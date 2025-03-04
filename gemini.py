# 구글 제미나이 AI
from google import genai
from dotenv import load_dotenv
import os
load_dotenv()

def aiai(text):
    client = genai.Client(api_key=os.getenv("GEMINI_KEY"))
    response = client.models.generate_content(model="gemini-2.0-flash", contents=text + ";선영이랑 둘도없는 친구 찬열이처럼 말해줘")   
    answer = response.text
    print(answer)
    return answer

if __name__=="__main__":
    aiai("gpt에 대해 설명해")