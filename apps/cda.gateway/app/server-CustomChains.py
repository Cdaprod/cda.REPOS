from fastapi import FastAPI
from langserve import add_routes
from chains.list_buckets_chain import ListBucketsChain
from chains.make_bucket_chain import MakeBucketChain
# Import other chains from the /chains/ directory

app = FastAPI()

# Initialize custom chains
list_buckets_chain = ListBucketsChain(...)
make_bucket_chain = MakeBucketChain(...)
# Initialize other chains

# Define API routes
add_routes(app, list_buckets_chain, path="/listbuckets")
add_routes(app, make_bucket_chain, path="/makebucket")
# Add routes for other chains

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
