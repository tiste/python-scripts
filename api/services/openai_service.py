from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()


def ask_chatgpt(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content
