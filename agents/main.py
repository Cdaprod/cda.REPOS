import asyncio
import os
from autogen import AssistantAgent, UserProxyAgent
from startup_developer import StartupDeveloper  # Assuming implementation of StartupDeveloper agent

# Initialize the StartupDeveloper agent
local_api_key = "your-local-llm-api-key"
local_model_name = "your-local-model-name"
local_base_url = "http://localhost:9999"
startup_dev = StartupDeveloper("StartupDev", local_api_key, local_model_name, local_base_url)

# Planner Agent
planner = AssistantAgent(
    name="planner",
    llm_config={"config_list": config_list},  # Config list as per your setup
    system_message="You are a helpful AI assistant..."  # Custom system message
)

# Assistant Agent
assistant = AssistantAgent(
    name="assistant",
    llm_config={
        "temperature": 0,
        "timeout": 600,
        "cache_seed": 42,
        "config_list": config_list,  # Config list as per your setup
        "functions": [{"name": "ask_planner", "description": "...", "parameters": {...}}],
    }
)

# UserProxy Agent
user_proxy = UserProxyAgent(
    name="user_proxy",
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=10,
    code_execution_config={"work_dir": "planning"},
    function_map={"ask_planner": lambda message: planner_user.initiate_chat(planner, message=message)}
)

# Function to run the startup development process
async def run_startup_developer(idea):
    return await startup_dev.develop_software(idea)

# Example usage
idea = "Develop a chatbot for customer support."
result = asyncio.run(run_startup_developer(idea))
