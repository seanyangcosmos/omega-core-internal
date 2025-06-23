import json

# 載入語義結構資料（結構格式請依實際資料調整）
with open('semantic-structure.json', 'r', encoding='utf-8') as f:
    structure_data = json.load(f)

# 結構假設格式示例
units = structure_data.get("units", [])
dependencies = structure_data.get("dependencies", [])

result = {
    "total_units": len(units),
    "total_dependencies": len(dependencies),
    "issues_detected": [],
    "overall_status": "trusted"
}

# 偵測孤立單位
unit_ids = {u['id'] for u in units}
linked_ids = set()

for dep in dependencies:
    linked_ids.add(dep['source'])
    linked_ids.add(dep['target'])

for uid in unit_ids:
    if uid not in linked_ids:
        result["issues_detected"].append(f"孤立單位：{uid}")

# 偵測依賴鏈斷裂
for dep in dependencies:
    if dep['source'] not in unit_ids or dep['target'] not in unit_ids:
        result["issues_detected"].append(f"依賴鏈斷裂：{dep}")

# 偵測主體性缺失
if not any(u.get('type') == 'subjectivity' for u in units):
    result["issues_detected"].append("主體性語義缺失")

# 總結判斷
if result["issues_detected"]:
    result["overall_status"] = "untrusted"

# 輸出報告
with open('semantic-trust-report.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print("語義可信任檢測完成，結果已輸出至 semantic-trust-report.json")
