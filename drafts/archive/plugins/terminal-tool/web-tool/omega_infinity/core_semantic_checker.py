def semantic_suspicion_check(sentence):
    """
    語意懷疑掃描：
    - 檢查是否出現明顯矛盾、因果錯亂、語意自打臉
    - 此版為簡化邏輯示範，未來可擴展容悖檢測
    """
    suspicion_message = "語意正常，未發現矛盾或懷疑。"

    contradiction_keywords = [
        ("因為下雨所以沒濕", "下雨與沒濕矛盾"),
        ("他昨天去看電影，卻整天沒離開家", "地點描述自我矛盾"),
        ("我說謊是真的", "語意自我打臉")
    ]

    for pair in contradiction_keywords:
        if pair[0] in sentence:
            suspicion_message = f"⚠️ 懷疑語意矛盾：{pair[1]}"
            break

    return suspicion_message

