# Use the official latest Ubuntu image as a parent image
FROM ubuntu:latest

# Update Ubuntu and install Python
RUN apt-get update && apt-get install -y python3 python3-pip

# Set the working directory in the container
WORKDIR /app/frontend

# Copy the requirements and install Python dependencies
COPY requirements.txt /app/frontend/
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of the codebase into the working directory
COPY . /app/frontend/

# Command to run the script
CMD ["python3", "cda_repos.py", "--service", "frontend"]
