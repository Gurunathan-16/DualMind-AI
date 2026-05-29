class ConversationMemory:

    def __init__(self):
        self.messages = []

    def add_message(self, role, content):

        self.messages.append({
            "role": role,
            "content": content
        })

    def get_context(self, limit=6):

        return self.messages[-limit:]