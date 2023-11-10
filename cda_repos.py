# Given the list of repositories provided by the user, we will fetch data from GitHub API for each.

import requests
from pydantic import BaseModel, ValidationError, HttpUrl
from typing import List, Optional
from datetime import datetime
import os
import subprocess
import json
import sys

import argparse

parser = argparse.ArgumentParser(description='Clone and deploy repositories based on runner or service.')
parser.add_argument('--runner', type=str, help='Specify the runner to deploy its services', choices=['frontend', 'backend', 'api'])
parser.add_argument('--service', type=str, help='Deploy a single service')
parser.add_argument('--dry-run', action='store_true', help='Run the script in dry-run mode without actual cloning')

args = parser.parse_args()

def get_repos_from_runner(runner_type):
    # Add the directory to sys.path
    runner_path = os.path.join(os.getcwd(), runner_type)
    sys.path.insert(1, runner_path)
    
    # Import the repos module from the given path
    try:
        repos_module = __import__('repos')
        return [repo for repo_list in vars(repos_module).values() if isinstance(repo_list, list) for repo in repo_list]
    except ModuleNotFoundError:
        print(f"No 'repos.py' module found in the {runner_type} directory.")
        return []
 
# repo_names = [
#     'cda.langchain-templates', 'cda.agents',
#     'cda.Juno', 'cda.actions',
#     'cda.data-lake', 'cda.ml-pipeline', 'cda.notebooks',
#     'cda.CMS_Automation_Pipeline', 'cda.ml-pipeline',
#     'cda.data', 'cda.databases', 'cda.s3',
#     'cda.docker', 'cda.kubernetes', 'cda.jenkins',
#     'cda.weaviate', 'cda.WeaviateApiFrontend', 'cda.webhooks',
#     'cda.Index-Videos',
#     'cda.dotfiles', 'cda.faas', 'cda.pull', 'cda.resumes', 'cda.snippets', 'cda.superagent', 'cda.ZoomVirtualOverlay', 'cda.knowledge-platform',
#     'cda.nginx'
# ]

# Define the Owner model
class Owner(BaseModel):
    name: str
    id: int
    type: str  

# Define the Repository model
class Repository(BaseModel):
    id: int
    node_id: str
    name: str
    full_name: str
    owner: Owner
    private: bool
    html_url: HttpUrl
    description: Optional[str]
    fork: bool
    url: HttpUrl
    created_at: datetime
    updated_at: datetime
    pushed_at: datetime
    git_url: str
    ssh_url: str
    clone_url: HttpUrl
    size: int
    stargazers_count: int
    watchers_count: int
    language: Optional[str]
    has_issues: bool
    has_projects: bool
    has_downloads: bool
    has_wiki: bool
    has_pages: bool
    forks_count: int
    mirror_url: Optional[HttpUrl]
    archived: bool
    disabled: bool
    open_issues_count: int
    license: Optional[str]
    allow_forking: bool
    is_template: bool
    topics: List[str]
    visibility: str 

class GitHubAPI:
    BASE_URL = 'https://api.github.com'

    def __init__(self, access_token: str):
        self.access_token = access_token
        self.headers = {
            'Authorization': f'token {self.access_token}',
            'Accept': 'application/vnd.github.v3+json',
        }

    def get_repository(self, repo_name: str) -> Repository:
        """
        Fetch repository data from GitHub and return a Repository object.
        """
        url = f"{self.BASE_URL}/repos/{repo_name}"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return Repository(**response.json())
        else:
            print(f"Failed to fetch repository {repo_name}: {response.status_code}")
            return None

    def clone_repository(self, repository: Repository):
        """
        Clone the given repository to the current working directory.
        """
        clone_url = repository.clone_url.replace('https://', f'https://{self.access_token}@')
        repo_path = os.path.join(os.getcwd(), repository.name)
        
        if not os.path.exists(repo_path):
            subprocess.run(["git", "clone", clone_url], check=True)
            print(f"Repository {repository.name} cloned into {repo_path}")
        else:
            print(f"Repository {repository.name} already exists in the current directory.")

    def generate_build_structure_json(self, repositories: List[Repository]):
        """
        Generate a JSON file of the build structure of the cloned repositories.
        """
        build_structure = {
            'repositories': [repo.dict() for repo in repositories]
        }
        with open('build_structure.json', 'w') as f:
            json.dump(build_structure, f, indent=2)
        print("Generated build_structure.json")
        
    def save_repo_data_as_json(self, repo_names, filename):
        repo_data_list = [
            self.get_repository(repo_name).dict() 
            for repo_name in repo_names 
            if self.get_repository(repo_name)
        ]
        with open(filename, 'w') as json_file:
            json.dump(repo_data_list, json_file, indent=4)
        print(f"Generated {filename} with repository data.")


if __name__ == '__main__':
    github_api = GitHubAPI(access_token=os.environ.get('GH_TOKEN'))
    
    if args.dry_run and args.runner:
        print(f"Dry run activated. Fetching data for the runner: {args.runner}")
        repo_names = get_repos_from_runner(args.runner)
        github_api.save_repo_data_as_json(repo_names, f"{args.runner}_runner.json")

 
    elif args.runner:
        # Load repos from the specified runner's repos.py file
        repo_names = get_repos_from_runner(args.runner)
        for repo_name in repo_names:
            repo_data = github_api.get_repository(repo_name)
            if repo_data:
                github_api.clone_repository(repo_data)
                # ... additional logic to handle successful cloning ...

    elif args.service:
        # Deploy a single service
        repo_data = github_api.get_repository(args.service)
        if repo_data:
            github_api.clone_repository(repo_data)
            # ... additional logic to handle successful cloning ...

    else:
        print("Please specify either --runner or --service with an optional --dry-run flag.")
