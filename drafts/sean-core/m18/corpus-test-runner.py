import yaml
import json

# 載入語料
with open('corpus-test-data.yaml', 'r', encoding='utf-8') as f:
    corpus_data = yaml.safe_load(f)

# 模擬規則邏輯（示意版，實際應連結 M18 規則庫）
def apply_rules(sentence):
    if "偏移" in sentence or "缺少依賴" in sentence:
        return False
    return True

results = []
passed = 0
failed = 0

# 批次檢測
for item in corpus_data['corpus_sentences']:
    sentence = item['sentence']
    rule_passed = apply_rules(sentence)

    if rule_passed:
        passed += 1
    else:
        failed += 1

    results.append({
        "id": item['id'],
        "rules_passed": rule_passed,
        "notes": "結構穩定" if rule_passed else "偵測到結構偏移或缺陷"
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
