class ChatMemory:
    def __init__(self):
        self.conversation = []

    def add_user_message(self, msg):
        self.conversation.append({"role": "user", "content": msg})

    def add_bot_message(self, msg):
        self.conversation.append({"role": "assistant", "content": msg})

    def get_conversation(self):
        return self.conversation
