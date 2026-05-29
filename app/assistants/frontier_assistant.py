from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

SYSTEM_PROMPT = """
You are a helpful AI personal assistant.
Answer clearly and safely.
"""

class FrontierAssistant:

    def __init__(self):

        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )

        self.history = []

    def chat(self, user_message):

        self.history.append({
            "role": "user",
            "content": user_message
        })

        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ] + self.history[-6:]

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.7,
            max_tokens=200
        )

        assistant_reply = response.choices[0].message.content

        self.history.append({
            "role": "assistant",
            "content": assistant_reply
        })

        return assistant_reply