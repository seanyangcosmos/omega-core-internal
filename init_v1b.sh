#!/bin/bash

BASE_DIR="docs/modules/v1b-semantic-display"

# 建立資料夾結構
mkdir -p "$BASE_DIR/controller"
mkdir -p "$BASE_DIR/core_engine"
mkdir -p "$BASE_DIR/gpt_module"
mkdir -p "$BASE_DIR/display"

# controller/v1b_output_block.py
cat > "$BASE_DIR/controller/v1b_output_block.py" << EOF
from core_engine.core_judgement import analyse_sentence
from gpt_module.gpt_advice_generator import generate_advice
from display.formatter import format_output

def run_v1b_pipeline(user_input):
    judgement = analyse_sentence(user_input)
    advice = generate_advice(user_input, judgement['type'])
    return format_output(judgement, advice)
EOF

# core_engine/core_judgement.py
cat > "$BASE_DIR/core_engine/core_judgement.py" << EOF
def analyse_sentence(text):
    if "溫度" in text:
        return {"type": "哲學語義", "合法": True, "說明": "屬於抽象類語義推論"}
    else:
        return {"type": "未知", "合法": False, "說明": "未能識別語義類型"}
EOF

# gpt_module/gpt_advice_generator.py
cat > "$BASE_DIR/gpt_module/gpt_advice_generator.py" << EOF
def generate_advice(text, semantic_type):
    if semantic_type == "哲學語義":
        return "建議引入哲學模型進行類比處理。"
    return "暫無建議。"
EOF

# display/formatter.py
cat > "$BASE_DIR/display/formatter.py" << EOF
def format_output(judgement, advice):
    return f"""
    [語義類型]：{judgement['type']}
    [判斷結果]：{'✓ 合法' if judgement['合法'] else '✗ 不合法'}
    [補充說明]：{judgement['說明']}
    [模擬建議]：{advice}
    """
EOF

# index.html
cat > "$BASE_DIR/index.html" << EOF
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>V1-B｜語義互動展示頁</title>
</head>
<body>
  <h1>V1-B｜語義互動展示頁</h1>
  <p>此頁為 Sean Yang Core V1-2 展示頁</p>
</body>
</html>
EOF

echo "✅ V1-B 展示模組已完整建立於：$BASE_DIR"
