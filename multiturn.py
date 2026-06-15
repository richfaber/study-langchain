import ollama
import os
from dotenv import load_dotenv

load_dotenv()
ollama_host = os.getenv("OLLAMA_HOST", "http://localhost:11434")

client = ollama.Client(host=ollama_host)

def get_ai_response(messages):
    response = client.chat(
        model="gemma3:4b",
        options={ "temperature": 0.9 },
        messages=messages,
    )
    return response.message.content

messages = [
    {
        "role": "system", "content": "너는 사용자를 도와주는 상담사야"
    },
]

while True:
    user_input = input("사용자: ")

    if user_input == "exit":
        break

    messages.append({ "role": "user", "content": user_input })
    ai_response = get_ai_response(messages)
    messages.append({ "role": "assistant", "content": ai_response })
    print("AI: " + ai_response)
    