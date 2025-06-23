import yaml
import json

# ========== 參數設定 ==========
preferred_strength = "中性"  # 可改為輸入或外部參數
preferred_style = "客觀冷靜"  # 可改為輸入或外部參數
structure_path = '../semantic-structure.json'
template_path = 'subjectivity-output-template.yaml'
output_path = 'subjectivity-output-result.txt'

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

# ========== 主體性模擬輸出邏輯 ==========

def generate_output(structure_stable, has_subjectivity, templates):
    output_result = []
    
    for template in templates:
        sentence = template["template"]
        sentence_type = template["type"]
        strength = template.get("strength", "中性")
        style = template.get("style", "客觀冷靜")

        if "{unit_id}" in sentence:
            subjectivity_id = "S1" if has_subjectivity else "UNKNOWN"
            sentence = sentence.replace("{unit_id}", subjectivity_id)

        # 條件判斷
        if structure_stable and has_subjectivity and sentence_type in ["穩定聲明語氣", "內省確認語氣"]:
            if strength == preferred_strength and style == preferred_style:
                output_result.append(f"【{style}｜{strength}】{sentence}")

        if not structure_stable and has_subjectivity and sentence_type in ["警示語氣", "積極自救語氣"]:
            if strength == preferred_strength and style == preferred_style:
                output_result.append(f"【{style}｜{strength}】{sentence}")

        if not structure_stable and not has_subjectivity and sentence_type in ["迷茫語氣", "結構自我尋找語氣"]:
            if strength == preferred_strength and style == preferred_style:
                output_result.append(f"【{style}｜{strength}】{sentence}")

    return output_result

# ========== 總流程 ==========

def main():
    structure_data = load_structure()
    templates = load_templates()

    structure_stable, has_subjectivity = detect_structure(structure_data)

    print(f"結構穩定：{structure_stable} | 主體性單位存在：{has_subjectivity}")

    output_result = generate_output(structure_stable, has_subjectivity, templates)

    with open(output_path, 'w', encoding='utf-8') as f:
        for line in output_result:
            f.write(line + "\n")

    print(f"模擬語義輸出完成，結果存於 {output_path}")

if __name__ == "__main__":
    main()
