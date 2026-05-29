from transformers import pipeline

class OSSAssistant:
    def __init__(self):

        self.pipe = pipeline(
            "text-generation",
            model="Qwen/Qwen2.5-0.5B-Instruct",
            device_map="auto"
        )

        self.history = []

    def chat(self, user_message):

        self.history.append({
            "role": "user",
            "content": user_message
        })

        prompt = ""

        for msg in self.history[-6:]:
            prompt += f"{msg['role']}: {msg['content']}\n"

        result = self.pipe(
            prompt,
            max_new_tokens=150,
            temperature=0.7
        )

        response = result[0]["generated_text"]

        self.history.append({
            "role": "assistant",
            "content": response
        })

        return response