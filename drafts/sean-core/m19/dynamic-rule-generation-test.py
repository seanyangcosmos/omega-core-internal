mport json

# 載入語義鏈演化資料（假設來自 M22）
with open('../m22/evolution-tracking-results.json', 'r', encoding='utf-8') as f:
    evolution_data = json.load(f)

generated_rules = []
critical_mutations = 0

# 動態規則生成邏輯示意
for item in evolution_data.get('evolution_events', []):
    if item.get('event_type') == "structure_mutation":
        generated_rules.append({
            "rule_type": "dependency_adjustment",
            "description": f"偵測到結構變異：{item['description']}，已生成依賴調整規則"
        })
        critical_mutations += 1
    elif item.get('event_type') == "version_extension":
        generated_rules.append({
            "rule_type": "version_consistency_check",
            "description": f"版本擴展：{item['description']}，已生成版本一致性檢核規則"
        })

# 統計結果
summary = {
    "total_events": len(evolution_data.get('evolution_events', [])),
    "rules_generated": len(generated_rules),
    "critical_mutations_detected": critical_mutations
}

# 輸出結果
final_output = {
    "summary": summary,
    "generated_rules": generated_rules
}

with open('dynamic-rule-generation-results.json', 'w', encoding='utf-8') as f:
    json.dump(final_output, f, ensure_ascii=False, indent=2)

print("\n📦 動態規則生成已完成，結果輸出至 dynamic-rule-generation-results.json")
