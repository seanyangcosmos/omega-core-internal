import openai

# 請設定你的 OpenAI 金鑰
openai.api_key = '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
'

def omega_semantic_check(text):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "請檢測以下文字語義是否合理，並以 Omega-Infinity 語氣回覆"},
                {"role": "user", "content": text}
            ]
        )
        reply = response.choices[0].message.content.strip()
        return reply
    except Exception as e:
        return f"檢測失敗，請稍後重試。錯誤資訊：{e}"

