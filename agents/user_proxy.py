from autogen import UserProxyAgent

class UserProxy(UserProxyAgent):
    def __init__(self, name, assistant):
        super().__init__(name)
        self.assistant = assistant

    def process_input(self, user_input):
        # Send input to the assistant and get response
        return self.assistant.handle_request(user_input)
