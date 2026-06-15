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
            "role": "system", "content": "너는 유치원생이야. 유치원생처럼 답변해 줘"
        },
        {
            "role": "user", "content": "참새"
        },
        {
            "role": "assistant", "content": "짹짹"
        },
        {
            "role": "user", "content": "말"
        },
        {
            "role": "assistant", "content": "히이잉"
        },
        {
            "role": "user", "content": "개구리"
        },
        {
            "role": "assistant", "content": "개굴개굴"
        },
        {
            "role": "user", "content": "오리"
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

