def detect_contradictions(text):
    problems = []
    
    # 簡單矛盾詞組範例，你可以自己擴充
    contradiction_patterns = [
        ["昨天出門", "整天沒離開家"],
        ["很餓", "不想吃東西"],
        ["請假", "來上班"],
        ["不想去", "已經去了"],
        ["今天", "不在家", "在家"]
    ]

    for pattern in contradiction_patterns:
        hit_count = 0
        for word in pattern:
            if word in text:
                hit_count += 1
        if hit_count >= 2:
            problems.append(f"語句內邏輯矛盾：同時出現 {', '.join(pattern)}")

    return problems
