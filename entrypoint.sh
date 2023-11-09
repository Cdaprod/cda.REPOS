#!/bin/bash

# REGISTRATION_TOKEN is expected to be provided as an environment variable
./config.sh --url https://github.com/<your-org>/<your-repo> --token ${REGISTRATION_TOKEN} --unattended --replace
./run.sh
