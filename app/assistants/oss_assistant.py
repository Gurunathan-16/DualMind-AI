from transformers import pipeline

class OSSAssistant:

    def __init__(self):

        self.pipe = pipeline(
            "text-generation",
            model="Qwen/Qwen2.5-0.5B-Instruct"
        )

        self.memory = []

    def chat(self, user_input):

        # Save user input
        self.memory.append(
            f"User: {user_input}"
        )

        # Short memory
        conversation = "\n".join(
            self.memory[-4:]
        )

        # Proper assistant prompt
        prompt = f"""
    ```

    You are a helpful AI assistant.

    {conversation}

    Assistant:
    """
        # Generate
        result = self.pipe(
            prompt,
            max_new_tokens=50,
            temperature=0.3,
            return_full_text=False
        )

        response = result[0]["generated_text"].strip()

        # Clean bad outputs
        response = response.replace("User:", "")
        response = response.replace("Assistant:", "")

        # Save response
        self.memory.append(
            f"Assistant: {response}"
        )

        return response
