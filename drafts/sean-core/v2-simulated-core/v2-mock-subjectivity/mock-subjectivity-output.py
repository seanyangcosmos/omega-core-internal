import yaml
import random

# 載入語義輸出範本
with open('subjectivity-output-template.yaml', 'r', encoding='utf-8') as f:
    templates = yaml.safe_load(f).get("output_templates", [])

# 模擬語義結構狀態
structure_status = random.choice(["穩定", "偏移"])

output_result = []

for template in templates:
    sentence = template["template"]

    # 若模板含變數，模擬填入主體性單位 ID
    if "{unit_id}" in sentence:
        sentence = sentence.replace("{unit_id}", "S1")

    # 模擬語義狀態影響語句輸出
    if structure_status == "穩定" and template["type"] == "穩定主體性語氣":
        output_result.append(sentence)
    elif structure_status == "偏移" and template["type"] == "警示語氣":
        output_result.append(sentence)
    elif template["type"] == "自我定位語氣":
        output_result.append(sentence)

# 輸出結果
with open('subjectivity-output-result.txt', 'w', encoding='utf-8') as f:
    for line in output_result:
        f.write(line + "\n")

print("語義主體性模擬語義輸出已完成，結果存於 subjectivity-output-result.txt")
