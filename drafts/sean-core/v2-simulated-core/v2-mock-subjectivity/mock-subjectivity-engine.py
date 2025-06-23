import yaml
import json

# 載入語義結構資料
with open('../semantic-structure.json', 'r', encoding='utf-8') as f:
    structure_data = json.load(f)

with open('subjectivity-structure.yaml', 'r', encoding='utf-8') as f:
    subjectivity_data = yaml.safe_load(f)

units = structure_data.get("units", [])
unit_ids = {u['id'] for u in units}
required_subjectivity_ids = {s['id'] for s in subjectivity_data.get("subjectivity_units", [])}

report = {
    "total_subjectivity_units_required": len(required_subjectivity_ids),
    "present_units": 0,
    "missing_units": [],
    "overall_status": "unstable"
}

for sid in required_subjectivity_ids:
    if sid in unit_ids:
        report["present_units"] += 1
    else:
        report["missing_units"].append(sid)

if not report["missing_units"]:
    report["overall_status"] = "stable"

# 輸出分析報告
with open('subjectivity-report.json', 'w', encoding='utf-8') as f:
    json.dump(report, f, ensure_ascii=False, indent=2)

print("語義主體性穩定性分析完成，結果輸出至 subjectivity-report.json")
