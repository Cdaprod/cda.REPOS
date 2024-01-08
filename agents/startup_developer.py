import os
import asyncio
from autogen import BaseAgent
from metagpt.roles import Architect, Engineer, ProductManager, ProjectManager
from metagpt.team import Team

# main-agents.py or a .ipynb file

# Import necessary modules
import asyncio
from startup_developer_agent import StartupDeveloper  # Assuming the agent code is in this file

# Define your local LLM details
# api_key = "your-local-llm-api-key"
# model_name = "your-local-model-name"
# base_url = "http://localhost:9999"

class StartupDeveloper(BaseAgent):
    def __init__(self, name, api_key, api_model, base_url):
        super().__init__(name)
        os.environ["OPENAI_API_KEY"] = api_key
        os.environ["OPENAI_API_MODEL"] = api_model
        os.environ["OPENAI_API_BASE"] = base_url  # Set your local LLM base URL

    async def develop_software(self, idea):
        company = Team()
        company.hire([ProductManager(), Architect(), ProjectManager(), Engineer()])
        company.invest(investment=3.0)
        company.run_project(idea=idea)

        await company.run(n_round=5)
        return company

# Initialize the StartupDeveloper agent
startup_dev = StartupDeveloper("MyStartupDev", api_key, model_name, base_url)

# Define the project idea
project_idea = "Develop an AI-powered content recommendation system."

# Run the development process asynchronously
software_project = asyncio.run(startup_dev.develop_software(project_idea))