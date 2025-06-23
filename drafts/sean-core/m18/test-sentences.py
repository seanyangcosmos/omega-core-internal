import json
import yaml
import os

# 自動判斷同檔名結果輸出
input_file = 'test-sentences.yaml'
result_file = os.path.splitext(input_file)[0] + '-results.json'

# 載入規則清單
with open('rule-checklist.yaml', 'r', encoding='utf-8') as f:
    rules_data = yaml.safe_load(f)

# 載入修正建議
with open('repair-suggestion.md', 'r', encoding='utf-8') as f:
    repair_text = f.read()

# 載入測試語句資料
with open(input_file, 'r', encoding='utf-8') as f:
    test_data = yaml.safe_load(f)

# 統計變數
total = 0
valid_count = 0
invalid_count = 0
violations_by_rule = {}
detailed_results = []

# 簡易規則比對函數
def check_sentence(sentence, context=None, allow_paradox=False):
    for rule in rules_data['rules']:
        if rule['id'] == 'SR-001' and "所有封閉系統皆收斂" in str(context) and "不收斂" in sentence:
            return rule, "請考慮弱化全稱語句或限定例外條件。"
        if rule['id'] == 'SR-002' and "↔ ¬" in sentence and not allow_paradox:
            return rule, "請明確標記容悖語句或結構分離。"
    return None, None

# 批次檢測
for idx, item in enumerate(test_data['sentences']):
    total += 1
    sentence = item.get("sentence")
    context = item.get("context", "")
    allow_paradox = item.get("allow_paradox", False)

    violation, suggestion = check_sentence(
        sentence=sentence,
        context=context,
        allow_paradox=allow_paradox
    )

    if violation:
        invalid_count += 1
        rule_id = violation['id']
        violations_by_rule[rule_id] = violations_by_rule.get(rule_id, 0) + 1

        detailed_results.append({
            "index": idx + 1,
            "sentence": sentence,
            "status": "invalid",
            "violation_type": violation['description'],
            "severity": violation['severity'],
            "suggested_repair": suggestion
        })
    else:
        valid_count += 1
        detailed_results.append({
            "index": idx + 1,
            "sentence": sentence,
            "status": "valid"
        })

# 統計輸出
summary = {
    "total": total,
    "valid": valid_count,
    "invalid": invalid_count,
    "violation_ratio_percent": round((invalid_count/total)*100, 2),
    "violations_by_rule": violations_by_rule,
    "detailed_results": detailed_results
}

# 寫入結果檔
with open(result_file, 'w', encoding='utf-8') as f:
    json.dump(summary, f, ensure_ascii=False, indent=2)

print(f"\n📦 結果已輸出至 {result_file}")
