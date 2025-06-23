import yaml
import json

# 載入語義結構資料
with open('../semantic-structure.json', 'r', encoding='utf-8') as f:
    structure_data = json.load(f)

# 載入語義輸出範本
with open('subjectivity-output-template.yaml', 'r', encoding='utf-8') as f:
    templates = yaml.safe_load(f).get("output_templates", [])

units = structure_data.get("units", [])
dependencies = structure_data.get("dependencies", [])

unit_ids = {u['id'] for u in units}
linked_ids = set()

# 偵測孤立單位
for dep in dependencies:
    linked_ids.add(dep['source'])
    linked_ids.add(dep['target'])

has_isolated = any(uid not in linked_ids for uid in unit_ids)

# 偵測主體性單位
subjectivity_units = [u['id'] for u in units if u.get('type') == 'subjectivity']
has_subjectivity = bool(subjectivity_units)

# 決定輸出語氣
output_result = []

for template in templates:
    sentence = template["template"]

    # 若模板含變數，模擬填入主體性單位 ID
    if "{unit_id}" in sentence:
        sentence = sentence.replace("{unit_id}", subjectivity_units[0] if has_subjectivity else "UNKNOWN")

    # 結構穩定情況
    if not has_isolated and has_subjectivity and template["type"] == "穩定主體性語氣":
        output_result.append(sentence)

    # 結構不穩定但主體性存在
    if has_isolated and has_subjectivity and template["type"] == "警示語氣":
        output_result.append(sentence)

    # 結構不穩定且主體性缺失
    if has_isolated and not has_subjectivity and template["type"] == "自我定位語氣":
        output_result.append(sentence)

# 輸出結果
with open('subjectivity-output-result.txt', 'w', encoding='utf-8') as f:
    for line in output_result:
        f.write(line + "\n")

print("語義主體性模擬語義輸出已完成，結果存於 subjectivity-output-result.txt")
