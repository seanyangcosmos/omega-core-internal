# controller/v1b_output_block.py
# 模組引用：M3 + M9 + M17 + GPT 模擬 + Formatter 格式器

from engine.core_judgement import evaluate_statement
from engine.gpt_advice_generator import generate_advice
from engine.formatter import format_output

def analyze_semantics(user_input: str) -> str:
    """
    主控制函數：分析語句語義、回傳格式化結果

    Parameters:
        user_input (str): 使用者輸入語句

    Returns:
        str: 統一格式結果（GPT模擬建議 + 系統語義判斷 + 引用模組）
    """

    # 🔍 1. 系統語義判準（引用 M3 + M9 + M17）
    judgement = evaluate_statement(user_input)

    # 🤖 2. GPT 模擬建議（補助意見，不具最終判斷權）
    gpt_opinion = generate_advice(user_input)

    # 📦 3. 整合輸出
    output = format_output(
        original=user_input,
        judgement=judgement,
        gpt_opinion=gpt_opinion,
        modules_used=["M3", "M9", "M17"]
    )

    return output
