from assistant import Assistant
from planner import Planner
from user_proxy import UserProxy
from startup_developer import StartupDeveloper
from custom_object_tool import CustomObjectTool

# Initialize components
startup_dev = StartupDeveloper(...)
custom_tool = CustomObjectTool(...)
planner = Planner("Planner", llm_config, startup_dev, custom_tool)
assistant = Assistant("Assistant", llm_config, planner)
user_proxy = UserProxy("UserProxy", assistant)

# Example usage
user_input = "I need a tool for analyzing data patterns."
response = user_proxy.process_input(user_input)
print(response)
