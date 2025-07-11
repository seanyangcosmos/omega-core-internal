# run_v1b.py（主控制器）🔧
# 將用戶輸入送進核心判斷與 GPT 模擬器，再整合格式輸出

from controller.v1b_output_block import analyze_semantics

if __name__ == "__main__":
    user_input = input("請輸入語句：")
    result = analyze_semantics(user_input)
    print(result)
