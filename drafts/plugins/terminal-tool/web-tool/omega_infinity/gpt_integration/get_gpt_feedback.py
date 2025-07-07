import openai
import os
from dotenv import load_dotenv

load_dotenv()

client = openai.Client(api_key=os.getenv("OPENAI_API_KEY"))

def get_gpt_feedback(sentence):
    prompt = (
        f"請針對以下句子進行詳細語義與結構檢查：\n"
        f"{sentence}\n"
        "要求：\n"
        "1. 結構合理性（語序、詞性、主詞動詞搭配）\n"
        "2. 語意合理性（邏輯、通順、是否含混）\n"
        "3. 基本語法結構（標點、完整性）\n"
        "請逐條回覆，每條前方標示『結構合理性：』、『語意合理性：』、『基本語法結構：』，最後請提供總結。"
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "你是語法與語義結構檢查助手，請依據規則逐條回覆。"},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500
    )

    return response.choices[0].message.content.strip()

