def process_text(text):
    if "測試" in text:
        return "需要進一步語義檢測"
    elif len(text.strip()) == 0:
        return "輸入為空，請重新輸入"
    else:
        return "本地判定：語句內容合理"



import openai

openai.api_key = "你的 GPT 金鑰"

def gpt_check(text):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "請判斷以下語句是否語義合理，簡潔回應『合理』或『不合理』。"},
                {"role": "user", "content": text}
            ]
        )
        result = response.choices[0].message.content.strip()
        return result
    except Exception as e:
        return f"GPT 請求失敗：{e}"
