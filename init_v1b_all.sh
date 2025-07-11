#!/bin/bash
BASE_DIR="docs/modules/v1b-semantic-display"
mkdir -p "$BASE_DIR"/{controller,core_engine,gpt_module,display}

# 1. 建立展示頁 index.html
cat << EOF > "$BASE_DIR/index.html"
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>V1-B 語義互動展示頁</title>
</head>
<body>
  <h1>V1-B 語義互動展示頁</h1>
  <p>此頁為 Sean Yang Core V1-2 展示頁</p>
</body>
</html>
EOF

# 2. 建立 CLI 程式 run_v1b.py
cat << EOF > "$BASE_DIR/run_v1b.py"
from controller.v1b_output_block import run_v1b_pipeline

if __name__ == "__main__":
    print("🚀 Sean Yang Core V1-B 語義互動 CLI 啟動")
    while True:
        user_input = input("請輸入語句（輸入 exit 結束）：")
        if user_input.lower() == "exit":
            print("👋 再見！")
            break
        result = run_v1b_pipeline(user_input)
        print(result)
EOF

# 3. 建立 v1b_output_block.py（控制器）
cat << EOF > "$BASE_DIR/controller/v1b_output_block.py"
from core_engine.core_judgement import analyse_subject_type
from gpt_module.gpt_advice_generator import generate_advice
from display.formatter import format_result

def run_v1b_pipeline(sentence):
    subject_type = analyse_subject_type(sentence)
    advice = generate_advice(sentence, subject_type)
    return format_result(sentence, subject_type, advice)
EOF

# 4. 建立 core_judgement.py（語義分析）
cat << EOF > "$BASE_DIR/core_engine/core_judgement.py"
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

EOF

# 5. 建立 gpt_advice_generator.py（GPT建議模組）
cat << EOF > "$BASE_DIR/gpt_module/gpt_advice_generator.py"
def generate_advice(sentence, subject_type):
    # 模擬 GPT 回應
    return f"模擬建議：針對「{subject_type}」的語義，建議進一步哲學判準。"
EOF

# 6. 建立 formatter.py（格式化輸出）
cat << EOF > "$BASE_DIR/display/formatter.py"
def format_result(sentence, subject_type, advice):
    return f"🧠 原句：「{sentence}」\\n🔍 主體類型：{subject_type}\\n💡 模擬建議：{advice}"
EOF

# 7. 自動在 docs/index.md 增加展示連結（若尚未包含）
INDEX_MD="docs/index.md"
LINK_MARKER="[V1-B 語義互動展示頁](modules/v1b-semantic-display/index.html)"
if ! grep -q "$LINK_MARKER" "$INDEX_MD"; then
  echo -e "\n## 🔗 模組展示區\n- $LINK_MARKER" >> "$INDEX_MD"
fi

echo "✅ V1-B 展示模組已完整建立於：$BASE_DIR"
