import yaml
import json

with open('self-repair-structure.yaml', 'r', encoding='utf-8') as f:
    rules = yaml.safe_load(f)['repair_rules']

result = {
    "total_rules": len(rules),
    "repairs_suggested": len(rules),
    "details": []
}

# 模擬所有偏移偵測並提出建議
for rule in rules:
    result['details'].append({
        "rule_id": rule['id'],
        "action": "建議補正",
        "description": rule['description']
    })

with open('semantic-repair-report.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print("語義偏移自我修正建議已生成，結果輸出至 semantic-repair-report.json")
