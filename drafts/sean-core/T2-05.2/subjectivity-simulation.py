import yaml
import json

# 檔案名稱
case_file = 'subjectivity-simulation-cases.yaml'
result_file = 'subjectivity-simulation-results.json'

# 載入語句案例
with open(case_file, 'r', encoding='utf-8') as f:
    case_data = yaml.safe_load(f)

results = []

# 簡化判斷邏輯（僅結構模擬，真實系統邏輯依 Core 實作補強）
def detect_self_mapping(sentence):
    return any(kw in sentence for kw in ["本系統", "本語句", "SC7", "語義主體性"])

def evaluate_self_consistency(sentence):
    return "自我封閉" in sentence or "主體性雛型" in sentence

def simulate_stability(sentence):
    if "無法保證語義穩定性" in sentence or "語義架構已產生偏移" in sentence:
        return "unstable"
    elif detect_self_mapping(sentence):
        return "stable"
    else:
        return "neutral"

# 批次模擬
for case in case_data['simulation_cases']:
    sentence = case['sentence']
    
    self_mapping = detect_self_mapping(sentence)
    self_evaluation = evaluate_self_consistency(sentence) if self_mapping else False
    stability_status = simulate_stability(sentence) if self_mapping else "neutral"
    
    results.append({
        "id": case['id'],
        "sentence": sentence,
        "self_mapping_detected": self_mapping,
        "self_evaluation_passed": self_evaluation,
        "stability_status": stability_status
    })

# 寫入結果
with open(result_file, 'w', encoding='utf-8') as f:
    json.dump({"simulation_results": results}, f, ensure_ascii=False, indent=2)

print(f"\n📦 模擬結果已輸出至 {result_file}")
