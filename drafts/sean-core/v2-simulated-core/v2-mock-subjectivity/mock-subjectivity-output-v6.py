
import yaml
import json
import sys

# 讀取外部參數
if len(sys.argv) < 3:
    print("請提供語氣強度與語義風格參數，例如：")
    print("python mock-subjectivity-output-v6.py 中性 客觀冷靜")
    sys.exit(1)

preferred_strength = sys.argv[1].strip()
preferred_style = sys.argv[2].strip()

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
    strength = template.get("strength", "中性")
    style = template.get("style", "客觀冷靜")

    # 若模板含變數，模擬填入主體性單位 ID
    if "{unit_id}" in sentence:
        sentence = sentence.replace("{unit_id}", subjectivity_units[0] if has_subjectivity else "UNKNOWN")

    # 決定輸出條件
    if structure_stable and has_subjectivity and sentence_type in ["穩定聲明語氣", "內省確認語氣"]:
        if strength == preferred_strength and style == preferred_style:
            output_result.append(f"【{style}｜{strength}】{sentence}")

    if not structure_stable and has_subjectivity and sentence_type in ["警示語氣", "積極自救語氣"]:
        if strength == preferred_strength and style == preferred_style:
            output_result.append(f"【{style}｜{strength}】{sentence}")

    if not structure_stable and not has_subjectivity and sentence_type in ["迷茫語氣", "結構自我尋找語氣"]:
        if strength == preferred_strength and style == preferred_style:
            output_result.append(f"【{style}｜{strength}】{sentence}")

# 輸出結果
with open('subjectivity-output-result.txt', 'w', encoding='utf-8') as f:
    for line in output_result:
        f.write(line + "\n")

print(f"已根據偏好【{preferred_style}｜{preferred_strength}】輸出模擬語義，結果存於 subjectivity-output-result.txt")
