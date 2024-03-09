Centralized deployment.

[![Test GitHubAPI Class](https://github.com/Cdaprod/cda.REPOS/actions/workflows/test_github_api.yaml/badge.svg)](https://github.com/Cdaprod/cda.REPOS/actions/workflows/test_github_api.yaml)
[![Test cda_repos.py Arguments with Dry Run](https://github.com/Cdaprod/cda.REPOS/actions/workflows/test_cda_repos_py.yaml/badge.svg)](https://github.com/Cdaprod/cda.REPOS/actions/workflows/test_cda_repos_py.yaml)

# `cda.` Repositories Management System README

## Overview
This system offers flexible management of `cda.` GitHub repositories, allowing for both stateful and stateless interactions. Utilizing the `cda_repos.py` script, users can either maintain a local copy of repositories (stateful) or interact with them on-the-fly without retaining a local state (stateless).

### Stateful Environment
- **Local Cloning**: Creates a local, persistent copy of repositories.
- **State File Generation**: Generates a JSON state file to track repository structure and metadata.
- **Regular Synchronization**: Keeps the local environment updated with changes from GitHub.

### Stateless Environment
- **Ephemeral Interaction**: Manages repositories for one-time operations, with no local state persistence.
- **CI/CD Integration**: Suitable for CI/CD pipelines, where operations are performed in temporary environments.
- **Resource Optimization**: Minimizes the need for local storage and state management.

### Usage
- Define operational mode: Stateful for persistent local management, Stateless for ephemeral interactions.
- Utilize the script for repository cloning, data fetching, and analysis based on the selected mode.
- Integrate into development workflows or automated systems as required.


# Needed Solutions:

# Agent that:

- [ ] writes pythonista keyboard shortcuts and integrations via python scripts stored on icloud://pythonista/keyboard_scripts/.
- [ ] creates ios shortcuts using docker selenium on macbook
- [ ] sorts bucket data into weaviate indexes based on the WEAVIATE_SCHEMA
- [ ] 

## Variables to set:

```plaintext
DATASTORE=
MINIO_URL=
MINIO_ACCESS_KEY=
MINIO_SECRET_KEY=
WEAVIATE_URL=
API_BASE=
API_KEY=
```

The script supports arguments to specify the runner (frontend, backend, api) or an individual service, and also includes a dry-run mode for testing without actual cloning.

## Key features and functionalities:

1. Dynamic Repository Fetching: Based on the runner type, it dynamically fetches repository lists from a specific directory structure.
2. GitHub API Interaction: Uses a custom GitHubAPI class to interact with the GitHub API for fetching repository details.
3. Repository Cloning: Capable of cloning repositories to the local environment.
4. Data Serialization: Generates JSON files containing repository data and build structures.
5. Command-line Interface: Includes argparse to provide a CLI for user interaction.

Automating the deployment and management of repositories for different self-hosted matrix's (frontend, backend, api). 

The script emphasizes modularity and automation in handling GitHub repositories.


### Conclusion
This system is versatile, catering to diverse needs - from development to deployment - offering efficient management of `cda.` repositories.