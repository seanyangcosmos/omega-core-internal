def check_gpt_content(text):
    keywords = [
        "GPT", "ChatGPT", "OpenAI", "生成式AI",
        "大型語言模型", "LLM", "GPT-4", "GPT-3.5",
        "prompt", "AI 對話", "自然語言生成", "文本生成"
    ]
    lower_text = text.lower()
    for kw in keywords:
        if kw.lower() in lower_text:
            return True
    return False
