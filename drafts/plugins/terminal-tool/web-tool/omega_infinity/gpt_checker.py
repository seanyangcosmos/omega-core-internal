def check_with_gpt(text):
    """
    模擬 GPT 處理邏輯。
    這裡未連線外部 API，之後可改進為真實呼叫。
    """
    if "GPT" in text.upper():
        return "判斷結果：GPT 相關內容"
    else:
        return "判斷結果：非 GPT 相關內容"



