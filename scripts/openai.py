import sys

from api.services.openai_service import ask_chatgpt


def main():
    prompt = " ".join(sys.argv[1:]) or "Hello, ChatGPT!"
    result = ask_chatgpt(prompt)
    print("Réponse OpenAI :", result)
