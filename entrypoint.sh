#!/bin/bash

# REGISTRATION_TOKEN is expected to be provided as an environment variable
./config.sh --url ${REPO_URL} --token ${RUNNER_TOKEN} --unattended --replace

./run.sh
