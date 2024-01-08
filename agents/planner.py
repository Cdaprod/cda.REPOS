import asyncio
from autogen import AssistantAgent
from startup_developer_agent import StartupDeveloper
from custom_object_tool import CustomObjectTool  # Replace with the actual import of your custom tool

class Planner(AssistantAgent):
    def __init__(self, name, llm_config, local_api_key, local_model_name, local_base_url):
        super().__init__(
            name=name,
            llm_config=llm_config,
            functions=[
                {
                    "name": "run_startup_developer",
                    "description": "Run the startup developer process.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "idea": {
                                "type": "string",
                                "description": "Idea for the startup developer to work on."
                            }
                        },
                        "required": ["idea"]
                    }
                },
                {
                    "name": "run_custom_object_tool",
                    "description": "Run the custom object tool process.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "parameters": {
                                "type": "object",
                                "description": "Parameters for the custom object tool."
                            }
                        },
                        "required": ["parameters"]
                    }
                }
            ]
        )
        self.startup_dev = StartupDeveloper("StartupDev", local_api_key, local_model_name, local_base_url)
        self.custom_tool = CustomObjectTool()  # Initialize your custom object tool

    async def run_startup_developer(self, idea):
        return await self.startup_dev.develop_software(idea)

    def run_custom_object_tool(self, parameters):
        return self.custom_tool.execute(parameters)  # Implement your custom tool logic

# Usage example
# planner = Planner("MyPlanner", llm_config, "your-local-llm-api-key", "your-local-model-name", "http://localhost:9999")
# result = asyncio.run(planner.run_startup_developer("Develop a chatbot for customer support."))
