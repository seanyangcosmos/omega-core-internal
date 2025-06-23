import json
import yaml

# 載入規則清單
with open('rule-checklist.yaml', 'r', encoding='utf-8') as f:
    rules_data = yaml.safe_load(f)

# 載入修正建議
with open('repair-suggestion.md', 'r', encoding='utf-8') as f:
    repair_text = f.read()

# 簡易規則比對函數（示意）
def check_sentence(sentence, context=None, allow_paradox=False):
    for rule in rules_data['rules']:
        if rule['id'] == 'SR-001' and "所有封閉系統皆收斂" in str(context) and "不收斂" in sentence:
            return rule, "請考慮弱化全稱語句或限定例外條件。"
        if rule['id'] == 'SR-002' and "↔ ¬" in sentence and not allow_paradox:
            return rule, "請明確標記容悖語句或結構分離。"
        # 其他規則可依此類推加入
    return None, None

# 測試輸入
test_input = {
    "sentence": "某些封閉系統不收斂。",
    "context": "所有封閉系統皆收斂。",
    "allow_paradox": False
}

# 執行檢測
violation, suggestion = check_sentence(
    sentence=test_input["sentence"],
    context=test_input["context"],
    allow_paradox=test_input["allow_paradox"]
)

# 輸出結果
if violation:
    print("⚠️ 檢測結果：不合法語句")
    print(f"違規類型：{violation['description']}")
    print(f"嚴重程度：{violation['severity']}")
    print(f"修正建議：{suggestion}")
else:
    print("✅ 語句合法，未檢測到違規。")
