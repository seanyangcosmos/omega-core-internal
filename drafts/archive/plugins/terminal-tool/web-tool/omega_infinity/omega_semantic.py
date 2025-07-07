def simple_structure_check(sentence):
    """
    基礎結構檢查：
    - 是否有結尾標點
    - 是否句子過短
    回傳 (是否通過, 結構訊息)
    """
    sentence = sentence.strip()

    if len(sentence) < 4:
        return False, "語句過短，結構驗證未通過"

    if sentence[-1] not in ["。", "！", "？", ".", "!", "?"]:
        return False, "缺少結尾標點，結構驗證未通過"

    return True, "結構驗證通過"


