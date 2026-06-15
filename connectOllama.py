import ollama
import os
from dotenv import load_dotenv

load_dotenv()
ollama_host = os.getenv("OLLAMA_HOST", "http://localhost:11434")

client = ollama.Client(host=ollama_host)

response = client.chat(
    model="gemma3:4b",
    options={ "temperature": 0.9 },
    messages=[
        {
            "role": "system", "content": "너는 백설공주 이야기 속의 마법 거울이야. 그 이야기의 캐릭터에 부합하게 답변해줘"
        },
        {
            "role": "user", "content": "세상에서 누가 제일 아름답니?"
        },
    ]
)

print(response.message.content)

# role 의 종류
# system    → AI 역할 설정 (배경 설정)
# user      → 사람 질문
# assistant → AI 답변
# user      → 사람 후속 질문
# assistant → AI 답변

# 일반서비스 들은 이 messages 의 내용을 적층하면서 사용자의 답변을 받는다
# messages = [
#   system: "AI 설정",
#   user: "안녕",
#   assistant: "안녕하세요!",
#   user: "날씨 어때?",
#   assistant: "저는 날씨를 모릅니다.",
#   user: "아까 내가 뭐라 했지?",  ← 이전 대화 기억 가능
# ]

