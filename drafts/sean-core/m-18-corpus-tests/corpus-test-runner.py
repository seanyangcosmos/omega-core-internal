import yaml
import json

# 模擬規則庫
rules = [
    {
        "type": "mandatory_dependency",
        "condition": lambda s: "SC7" in s,
        "description": "語句須明確標示依賴 SC7 結構"
    },
    {
        "type": "stability_constraint",
        "condition": lambda s: "偏移" not in s and "缺少依賴" not in s,
        "description": "語句不得出現結構偏移或依賴缺陷表述"
    },
    {
        "type": "self_closure_check",
        "condition": lambda s: "自我封閉" in s or "主體性雛型" in s,
        "description": "語句需具備自我封閉或主體性雛型描述"
    }
]

# 載入語料
with open('corpus-test-data.yaml', 'r', encoding='utf-8') as f:
    corpus_data = yaml.safe_load(f)

results = []
passed = 0
failed = 0

# 批次檢測
for item in corpus_data['corpus_sentences']:
    sentence = item['sentence']
    violations = []

    for rule in rules:
        if not rule['condition'](sentence):
            violations.append(rule['description'])

    rule_passed = len(violations) == 0

    if rule_passed:
        passed += 1
    else:
        failed += 1

    results.append({
        "id": item['id'],
        "rules_passed": rule_passed,
        "violations": violations,
        "notes": "結構穩定" if rule_passed else f"違反規則：{violations}"
    })

# 統計與輸出
summary = {
    "total_sentences": len(corpus_data['corpus_sentences']),
    "rules_passed": passed,
    "rules_failed": failed,
    "overall_status": "stable" if failed == 0 else "partially stable"
}

final_output = {
    "summary": summary,
    "details": results
}

with open('corpus-test-results.json', 'w', encoding='utf-8') as f:
    json.dump(final_output, f, ensure_ascii=False, indent=2)

print("\n📦 語料測試已完成，結果輸出至 corpus-test-results.json")
