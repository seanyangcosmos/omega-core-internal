# core_engine/core_judgement.py
# 核心語義判斷模組：引用 M3（結構邏輯）+ M9（語用合法性）+ M17（一致性偵測）

def evaluate_statement(statement: str) -> dict:
    """
    使用核心語義模組分析語句。

    Parameters:
        statement (str): 輸入語句

    Returns:
        dict: 判斷結果（類型、結果、補充說明、系統備註）
    """

    # 🧠 模組 M3：結構語法分類
    if "如果" in statement or "則" in statement:
        semantic_type = "條件推論型"
    elif "不可能" in statement or "必然" in statement:
        semantic_type = "模態語句"
    elif "自我" in statement or "我是" in statement:
        semantic_type = "主體判斷型"
    else:
        semantic_type = "一般敘述型"

    # ✅ 模組 M9：基本語用合法性判準
    if statement.strip() == "":
        result = "非法"
        remark = "語句為空"
    elif len(statement) < 4:
        result = "可疑"
        remark = "語句過短，無法判斷語義結構"
    else:
        result = "合法"
        remark = "語句符合最小語用結構"

    # 🔍 模組 M17：語義一致性提醒（此處可擴充）
    # ⚠ 若需實作跨語句一致性追蹤可引入外部上下文
    consistency = "無跨語句衝突（模組內一致）"

    return {
        "語義類型": semantic_type,
        "判斷結果": result,
        "補充說明": remark,
        "系統語義備註": consistency
    }
