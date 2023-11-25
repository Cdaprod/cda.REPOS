import uuid
import json
import logging
from flask import Flask, request, jsonify, abort
from minio import Minio, S3Error
import requests
from functools import wraps

app = Flask(__name__)

# Configure Logging
logging.basicConfig(level=logging.INFO)

def require_apikey(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        if request.headers.get('X-API-KEY') and request.headers.get('X-API-KEY') == "Your-API-Key":
            return view_function(*args, **kwargs)
        else:
            abort(401)
    return decorated_function
    

# Initialize MinIO client
minio_client = Minio(
    "minio-server:port",
    access_key="your-access-key",
    secret_key="your-secret-key",
    secure=False  # Set True for HTTPS
)

# Ensure MinIO Memory Bucket Exists
memory_bucket = "memory"
try:
    if not minio_client.bucket_exists(memory_bucket):
        minio_client.make_bucket(memory_bucket)
except S3Error as e:
    logging.error(f"MinIO Error: {e}")
    # Decide how to handle the startup error - exit or continue

# Function to dump data into MinIO memory bucket
def dump_to_memory(data):
    try:
        file_name = f"{uuid.uuid4()}.json"
        data_json = json.dumps(data)
        minio_client.put_object(memory_bucket, file_name, data_json, len(data_json))
    except S3Error as e:
        logging.error(f"Error writing to MinIO: {e}")

# Canopy Chat Endpoint
@require_apikey
@app.route('/chat', methods=['POST'])
def chat():
    chat_data = request.json

    # Basic validation of chat data
    if not isinstance(chat_data, dict) or 'message' not in chat_data:
        abort(400, description="Invalid chat data format.")

    try:
        canopy_response = requests.post("http://canopy-service/chat", json=chat_data)
        response_data = canopy_response.json()
        dump_to_memory({"request": chat_data, "response": response_data})
        return jsonify(response_data)
    except requests.RequestException as e:
        logging.error(f"Canopy Service Error: {e}")
        abort(500, description="Error communicating with Canopy service.")

# Memory Retrieval Endpoint
@require_apikey
@app.route('/memory', methods=['GET'])
def get_memory():
    try:
        objects = minio_client.list_objects(memory_bucket)
        history = [minio_client.get_object(memory_bucket, obj.object_name).data.decode() for obj in objects]
        return jsonify(history)
    except S3Error as e:
        logging.error(f"Error retrieving memory from MinIO: {e}")
        abort(500, description="Error accessing memory data.")

# Custom Processing Endpoint
@require_apikey
@app.route('/process', methods=['POST'])
def process_data():
    process_data = request.json

    # Implement custom logic for processing the data
    # This could be additional data manipulation, calling other services, etc.
    # For example:
    # processed_data = some_custom_processing_function(process_data)
    
    # Assuming the function returns a JSON-serializable object
    return jsonify(processed_data)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
