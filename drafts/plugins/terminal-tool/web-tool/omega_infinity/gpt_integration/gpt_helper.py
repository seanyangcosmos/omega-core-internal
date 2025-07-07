import openai
import os
from dotenv import load_dotenv

load_dotenv()

client = openai.Client(api_key=os.getenv("OPENAI_API_KEY"))

def get_gpt_feedback(sentence):
    prompt = (
        "請針對以下語句，從語義合理性角度進行判斷，結構如下：\n"
        "語句：「" + sentence + "」\n"
        "請明確回答：語義合理 或 語義不合理，並簡短說明原因。"
    )

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0
        )
        gpt_reply = response.choices[0].message.content.strip()
        return gpt_reply

    except Exception as e:
        return f"GPT 回應失敗：{str(e)}"
