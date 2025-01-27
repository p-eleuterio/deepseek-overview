from dotenv import load_dotenv
from openai import OpenAI
import os

# Load environment variables from the .env file
load_dotenv()

api_key = os.getenv('DS_API_KEY')

# Verify that api_key is correctly retrieved
if api_key:
    print("API Key retrieved successfully.")
else:
    print("API Key not found.")

#deepsek
client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

# Round 1
messages = [{"role": "user", "content": "9.11 and 9.8, which is greater?"}]
response = client.chat.completions.create(
    model="deepseek-reasoner",
    messages=messages,
    max_tokens=2040
)

reasoning_content = response.choices[0].message.reasoning_content
content = response.choices[0].message.content

## Round 2
#messages.append({'role': 'assistant', 'content': content})
#messages.append({'role': 'user', 'content': "How many Rs are there in the word 'strawberry'?"})
#response = client.chat.completions.create(
#    model="deepseek-reasoner",
#    messages=messages
#)
# ...