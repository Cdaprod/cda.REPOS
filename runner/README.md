# GitHub Actions Self-Hosted Runner Dockerfile

## Overview
This Dockerfile configures a self-hosted runner for GitHub Actions. It is based on Ubuntu and includes necessary tools like `curl`, `sudo`, `git`, and `jq`.

## Usage
1. **Build the Docker Image**:
   - Use `docker build` with the necessary build arguments (`REPO_URL` and `RUNNER_TOKEN`).
2. **Run the Container**:
   - Deploy the container in your environment, and it will connect to the specified GitHub repository as a runner.

## Building the Image
```bash
docker build -t github-runner --build-arg REPO_URL=<your-repo-url> --build-arg RUNNER_TOKEN=<your-runner-token> .

Deploying the Runner

Run the container using:

docker run -d --name my-runner github-runner

Customization

You can modify the Dockerfile to include additional dependencies or configurations as needed for your CI/CD tasks.

Author

Created by Cdaprod