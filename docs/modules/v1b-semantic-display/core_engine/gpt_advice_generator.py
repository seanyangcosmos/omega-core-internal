# core_engine/gpt_advice_generator.py
# 模組功能：呼叫 GPT 模擬意見（輔助語義建議，不具主體判斷權）

def generate_advice(user_input: str) -> str:
    """
    用 GPT 模擬一段語義建議（非判準、僅供展示）

    Parameters:
        user_input (str): 使用者輸入語句

    Returns:
        str: GPT 模擬建議（文字描述）
    """

    # ✅ 示意版本（可接入真實 GPT API）
    if "自我" in user_input or "我是" in user_input:
        suggestion = "這句話可能涉及主體性問題，建議補充上下文來釐清『自我』的定義。"
    elif "不可能" in user_input:
        suggestion = "你可能在使用模態語氣，建議明確定義條件或背景。"
    else:
        suggestion = "這句語義大致清晰，建議可進一步補充對象或因果邏輯。"

    return f"GPT 模擬建議：{suggestion}"
