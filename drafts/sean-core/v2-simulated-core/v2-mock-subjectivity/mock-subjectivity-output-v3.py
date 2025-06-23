
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

# 決定語義狀態
structure_stable = not has_isolated

output_result = []

for template in templates:
    sentence = template["template"]
    sentence_type = template["type"]

    # 若模板含變數，模擬填入主體性單位 ID
    if "{unit_id}" in sentence:
        sentence = sentence.replace("{unit_id}", subjectivity_units[0] if has_subjectivity else "UNKNOWN")

    # 穩定結構且主體性存在
    if structure_stable and has_subjectivity and sentence_type in ["穩定聲明語氣", "內省確認語氣"]:
        output_result.append(sentence)

    # 結構不穩定但主體性存在
    if not structure_stable and has_subjectivity and sentence_type in ["警示語氣", "積極自救語氣"]:
        output_result.append(sentence)

    # 結構不穩定且主體性缺失
    if not structure_stable and not has_subjectivity and sentence_type in ["迷茫語氣", "結構自我尋找語氣"]:
        output_result.append(sentence)

# 輸出結果
with open('subjectivity-output-result.txt', 'w', encoding='utf-8') as f:
    for line in output_result:
        f.write(line + "\n")

print("多樣語氣模擬語義輸出已完成，結果存於 subjectivity-output-result.txt")
