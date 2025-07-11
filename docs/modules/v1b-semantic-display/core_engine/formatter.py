# core_engine/formatter.py
# 模組功能：整合輸出格式（真實判準 + GPT 模擬 + 原始語句）

def format_output(original: str, judgement: dict, gpt_opinion: str, modules_used: list) -> str:
    """
    將語義分析與模擬建議整合為統一回覆格式。

    Parameters:
        original (str): 使用者原始語句
        judgement (dict): 語義判準回傳資料（來自 core_judgement）
        gpt_opinion (str): GPT 模擬建議
        modules_used (list): 使用模組名稱列表（例如 ["M3", "M9", "M17"]）

    Returns:
        str: 格式化文字回覆（適合展示頁用）
    """

    formatted = (
        f"\n【原始語句】：{original}\n"
        f"【語義類型】：{judgement.get('語義類型')}\n"
        f"【判斷結果】：{judgement.get('判斷結果')}\n"
        f"【補充說明】：{judgement.get('補充說明')}\n"
        f"【系統語義備註】：{judgement.get('系統語義備註')}\n"
        f"【GPT 模擬建議】：{gpt_opinion}\n"
        f"【引用模組】：{', '.join(modules_used)}"
    )
    return formatted
