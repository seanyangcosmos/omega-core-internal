def check_gpt_content(text):
    """
    檢測輸入內容是否與 GPT 或生成式 AI 相關
    """
    # 定義 GPT 相關關鍵詞
    keywords = [
        "GPT", "ChatGPT", "OpenAI", "生成式 AI", 
        "大型語言模型", "LLM", "GPT-4", "GPT-3.5", 
        "prompt", "AI 對話", "自然語言生成", "文本生成"
    ]

    # 統一轉小寫比對，避免大小寫誤判
    lower_text = text.lower()

    # 檢查是否包含任一關鍵詞
    for kw in keywords:
        if kw.lower() in lower_text:
            return True

    return False
