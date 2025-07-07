import openai
import os
from dotenv import load_dotenv

# 載入 .env 路徑
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))
openai_api_key = os.getenv("OPENAI_API_KEY")

from openai import OpenAI

client = OpenAI(api_key=openai_api_key)

def check_gpt_content(text):
    # 嚴格限制回答格式
    prompt = f"請你只用「是」或「否」兩個字回答，以下內容是否與 GPT、AI 生成式技術有關：\n\"{text}\""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        answer = response.choices[0].message.content.strip()
        print(f"GPT 回覆：{answer}")
        return answer == "是"
    except Exception as e:
        print(f"語意檢測錯誤：{e}")
        print(f"讀入金鑰：{openai_api_key}")
        return False
