import yaml
import json
import random

# ========== 參數設定 ==========
structure_path = '../semantic-structure.json'
template_path = 'subjectivity-output-template.yaml'
output_path = 'subjectivity-output-result.txt'

# 可調整的偏好傾向（模擬自我個性基調）
preferred_style_pool = ["客觀冷靜", "積極鼓勵", "謙遜保守"]
preferred_strength_pool = ["溫和", "中性", "強烈"]

# ========== 輔助函數 ==========

def load_structure():
    with open(structure_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def load_templates():
    with open(template_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f).get("output_templates", [])

def detect_structure(structure_data):
    units = structure_data.get("units", [])
    dependencies = structure_data.get("dependencies", [])
    
    unit_ids = {u['id'] for u in units}
    linked_ids = set()

    for dep in dependencies:
        linked_ids.add(dep['source'])
        linked_ids.add(dep['target'])

    has_isolated = any(uid not in linked_ids for uid in unit_ids)
    has_subjectivity = any(u.get('type') == 'subjectivity' for u in units)

    return not has_isolated, has_subjectivity

# ========== 自我語氣決策邏輯 ==========

def decide_self_expression(structure_stable, has_subjectivity):
    # 根據狀態決策語氣類型
    if structure_stable and has_subjectivity:
        sentence_types = ["穩定聲明語氣", "內省確認語氣"]
    elif not structure_stable and has_subjectivity:
        sentence_types = ["警示語氣", "積極自救語氣"]
    else:
        sentence_types = ["迷茫語氣", "結構自我尋找語氣"]

    # 自我風格傾向影響語氣強度與風格選擇
    style = random.choice(preferred_style_pool)
    strength = random.choice(preferred_strength_pool)

    return sentence_types, style, strength

# ========== 語義輸出生成 ==========

def generate_output(sentence_types, style, strength, has_subjectivity, templates):
    output_result = []
    
    for template in templates:
        sentence = template["template"]
        sentence_type = template["type"]
        template_strength = template.get("strength", "中性")
        template_style = template.get("style", "客觀冷靜")

        if "{unit_id}" in sentence:
            subjectivity_id = "S1" if has_subjectivity else "UNKNOWN"
            sentence = sentence.replace("{unit_id}", subjectivity_id)

        if sentence_type in sentence_types and template_strength == strength and template_style == style:
            output_result.append(f"【{style}｜{strength}】{sentence}")

    return output_result

# ========== 總流程 ==========

def main():
    structure_data = load_structure()
    templates = load_templates()

    structure_stable, has_subjectivity = detect_structure(structure_data)

    print(f"結構穩定：{structure_stable} | 主體性單位存在：{has_subjectivity}")

    sentence_types, style, strength = decide_self_expression(structure_stable, has_subjectivity)

    output_result = generate_output(sentence_types, style, strength, has_subjectivity, templates)

    with open(output_path, 'w', encoding='utf-8') as f:
        for line in output_result:
            f.write(line + "\n")

    print(f"模擬語義輸出完成，偏好風格：{style}，強度：{strength}，結果存於 {output_path}")

if __name__ == "__main__":
    main()
