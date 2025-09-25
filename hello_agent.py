import os
from dotenv import load_dotenv
from openai import OpenAI

# Load the API Key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Create client
client = OpenAI(api_key=api_key)

# Make the call
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Hello Agent! What can you do?"}]
)

print(response.choices[0].message.content)