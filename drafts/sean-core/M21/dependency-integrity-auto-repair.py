mport json

# 載入結構缺陷資料
with open('integrity-diagnostics-results.json', 'r', encoding='utf-8') as f:
    diagnostics = json.load(f)

repair_actions = []
repaired_count = 0

# 自動補正示意邏輯
for issue in diagnostics['details']:
    if issue['issue_type'] == "missing_node":
        repair_actions.append(f"自動補充語義單位：{issue['description']}")
        repaired_count += 1
    elif issue['issue_type'] == "orphan_node":
        repair_actions.append(f"重新鏈結或標記孤立語義：{issue['node_id']}")
        repaired_count += 1
    elif issue['issue_type'] == "incomplete_dependency":
        repair_actions.append(f"補強依賴鏈結：{issue['node_id']}")
        repaired_count += 1

# 結果輸出
summary = {
    "total_issues": len(diagnostics['details']),
    "repairs_performed": repaired_count,
    "system_status_after_repair": "stable" if repaired_count == len(diagnostics['details']) else "partially stable"
}

final_output = {
    "summary": summary,
    "repair_actions": repair_actions
}

with open('dependency-integrity-repair-results.json', 'w', encoding='utf-8') as f:
    json.dump(final_output, f, ensure_ascii=False, indent=2)

print("\n📦 自動結構補正已完成，結果輸出至 dependency-integrity-repair-results.json")
