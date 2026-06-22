import ollama
import os
from dotenv import load_dotenv

load_dotenv()
ollama_host = os.getenv("OLLAMA_HOST", "http://localhost:11434")

def summarize_txt(file_path: str):
    client = ollama.Client(host=ollama_host)
    
    with open(file_path, 'r', encoding='utf-8') as f:
        txt = f.read()

    system_prompt = f'''
    너는 다음 글을 요약하는 봇이다. 아래 글을 읽고, 저자의 문제 인식과 주장을 파악하고, 주요 내용을 요약하라.

    작성해야 하는 포맷은 다음과 같다.

    # 제목

    ## 저자의 문제 인식 및 주장 (15문장 이내)

    ============= 이하 텍스트 ================

    { txt }
    '''

    # print(system_prompt)
    # print('====================================')

    response = client.chat(
        model="gemma3:4b",
        options={ "temperature": 0.1, "num_ctx": 16384 }, 
        # num_ctx (컨텐스트 윈도우): 입력 + 출력 생성을 합친 전체 토큰 한도. 물리적으로 가능한 상한선
        # num_predict (생성 토큰 제한): 모델이 한번에 생성할 수 있는 최대 토큰 수 기본값 -1 (무제한). 내가 원하는 답변의 상한선
        messages= [
            { "role": "system", "content": system_prompt }
        ]
    )

    return response.message.content 

if __name__ == '__main__':
    file_path = 'sample.txt'

    summary = summarize_txt(file_path)
    print(summary)

    with open('./sample_summary.txt', 'w', encoding='utf-8') as f:
        f.write(summary)