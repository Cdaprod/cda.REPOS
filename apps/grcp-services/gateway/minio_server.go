package main

import (
    "context"
    "log"
    "net/http"
    "github.com/minio/minio-go/v7"
    "github.com/minio/minio-go/v7/pkg/credentials"
    pb "path/to/generated/protobuf/minio"
    "google.golang.org/grpc"
)

type minioServer struct {
    pb.UnimplementedMinioServiceServer
    minioClient *minio.Client
}

func newMinioClient() *minio.Client {
    client, err := minio.New("minio-server:port", &minio.Options{
        Creds:  credentials.NewStaticV4("accessKey", "secretKey", ""),
        Secure: false, // or true if using HTTPS
    })
    if err != nil {
        log.Fatalf("Failed to create MinIO client: %v", err)
    }
    return client
}

func (s *minioServer) UploadObject(ctx context.Context, in *pb.UploadObjectRequest) (*pb.UploadObjectResponse, error) {
    // Implement object upload logic using MinIO client
    _, err := s.minioClient.PutObject(ctx, in.BucketName, in.ObjectName, bytes.NewReader(in.Data), int64(len(in.Data)), minio.PutObjectOptions{})
    if err != nil {
        return nil, err
    }
    return &pb.UploadObjectResponse{Message: "Upload successful"}, nil
}

func (s *minioServer) DownloadObject(ctx context.Context, in *pb.DownloadObjectRequest) (*pb.DownloadObjectResponse, error) {
    // Implement object download logic using MinIO client
    object, err := s.minioClient.GetObject(ctx, in.BucketName, in.ObjectName, minio.GetObjectOptions{})
    if err != nil {
        return nil, err
    }
    data, err := ioutil.ReadAll(object)
    if err != nil {
        return nil, err
    }
    return &pb.DownloadObjectResponse{Data: data}, nil
}

func main() {
    lis, err := net.Listen("tcp", ":50051")
    if err != nil {
        log.Fatalf("Failed to listen: %v", err)
    }
    var opts []grpc.ServerOption
    grpcServer := grpc.NewServer(opts...)
    minioClient := newMinioClient()
    pb.RegisterMinioServiceServer(grpcServer, &minioServer{minioClient: minioClient})
    grpcServer.Serve(lis)
}
