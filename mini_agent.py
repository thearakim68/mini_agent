import os
from dotenv import load_dotenv
from openai import OpenAI

# Load .env API key
load_dotenv()
client = OpenAI()

# Define some sample tasks
tasks = [
    "Check today's weather in Phnom Penh, Cambodia",
    "Summarize the latest AI news",
    "Translate 'How are you?' to Khmer Language",
]

# Agent behavior
for task in tasks:
    print(f"/n🧠 [Agent received task]: {task}")
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful research assistant."},
            {"role": "user", "content": f"Please {task}"}
        ]
    )
    print("🗣️ [Agent output]:", response.choices[0].message.content)