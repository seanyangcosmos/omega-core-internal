def analyse_subject_type(sentence):
    SUBJECT_TYPE_DB = {
        "思想": "抽象過程",
        "靈魂": "哲學抽象體",
        "概念": "語義抽象體",
        "人體": "生物實體",
        "月球": "天體",
        "記憶": "抽象過程",
        "能量": "物理量",
        "空間": "物理場",
        "未來": "時間指涉物"
    }
    for key in SUBJECT_TYPE_DB:
        if key in sentence:
            return SUBJECT_TYPE_DB[key]
    return "未知語義型"

