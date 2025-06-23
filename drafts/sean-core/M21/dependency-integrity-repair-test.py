import json

# 載入缺陷診斷結果
with open('integrity-diagnostics-results.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

repair_actions = []
repaired_count = 0

# 補正邏輯示意（正式版本將結合語義結構）
for issue in data['details']:
    if issue['issue_type'] == "missing_node":
        repair_actions.append(f"補充語義單位：{issue['description']}")
        repaired_count += 1
    elif issue['issue_type'] == "orphan_node":
        repair_actions.append(f"評估刪除或重新鏈結：{issue['node_id']}")
        repaired_count += 1
    elif issue['issue_type'] == "incomplete_dependency":
        repair_actions.append(f"補強依賴結構：{issue['node_id']}")
        repaired_count += 1

# 結果輸出
repair_summary = {
    "total_issues_detected": len(data['details']),
    "total_repairs_suggested": repaired_count,
    "repair_actions": repair_actions,
    "system_status_after_repair": "stable" if repaired_count == len(data['details']) else "partially stable"
}

with open('integrity-repair-suggestions.md', 'w', encoding='utf-8') as f:
    f.write("# 語義鏈結構補正建議\n\n")
    for action in repair_actions:
        f.write(f"- {action}\n")
    f.write(f"\n系統補正後狀態：{repair_summary['system_status_after_repair']}\n")

print("\n📦 補正建議已輸出至 integrity-repair-suggestions.md")
