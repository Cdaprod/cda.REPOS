from autogen import AssistantAgent
from planner import Planner  # Assuming planner.py contains the Planner class

class Assistant(AssistantAgent):
    def __init__(self, name, llm_config):
        super().__init__(
            name=name,
            llm_config=llm_config,
            functions=[
                {
                    "name": "consult_planner",
                    "description": "Consult the planner for strategic decisions.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "message": {
                                "type": "string",
                                "description": "Message to send to the planner."
                            }
                        },
                        "required": ["message"]
                    }
                }
            ]
        )
        self.planner = Planner("Planner", llm_config, "local-api-key", "local-model-name", "http://localhost:9999")

    def consult_planner(self, message):
        # Logic to interact with the planner
        # This could involve sending a message to the planner and receiving a response
        return self.planner.run_startup_developer(message)

# Usage example
# assistant = Assistant("MyAssistant", llm_config)
# response = assistant.consult_planner("Develop a new feature for our application.")
