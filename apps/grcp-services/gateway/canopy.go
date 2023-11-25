package main

import (
    "bytes"
    "encoding/json"
    "net/http"
    "log"
)

// Define the structure for your request and response
type CanopyRequest struct {
    // Fields corresponding to your Flask endpoint's expected request
}

type CanopyResponse struct {
    // Fields corresponding to your Flask endpoint's response
}

func callCanopyService(canopyReq CanopyRequest) (CanopyResponse, error) {
    requestBody, err := json.Marshal(canopyReq)
    if err != nil {
        return CanopyResponse{}, err
    }

    resp, err := http.Post("http://localhost:5000/canopy_endpoint", "application/json", bytes.NewBuffer(requestBody))
    if err != nil {
        return CanopyResponse{}, err
    }
    defer resp.Body.Close()

    var canopyResp CanopyResponse
    if err := json.NewDecoder(resp.Body).Decode(&canopyResp); err != nil {
        return CanopyResponse{}, err
    }

    return canopyResp, nil
}

// Use callCanopyService in your gRPC service handlers
