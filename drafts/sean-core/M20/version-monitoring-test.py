import yaml
import json

# 載入語義鏈結構資料
with open('semantic-dependency-map.yaml', 'r', encoding='utf-8') as f:
    map_data = yaml.safe_load(f)

results = []
drift_count = 0

# 簡易檢測邏輯（示意版）
for warning in map_data['semantic_dependency_map'].get('drift_warnings', []):
    drift_count += 1
    results.append({
        "source": warning['source'],
        "affected": warning['affected'],
        "description": warning['description'],
        "status": "semantic drift detected"
    })

# 統計總結
summary = {
    "total_nodes": len(map_data['semantic_dependency_map']['nodes']),
    "total_drift_warnings": drift_count,
    "system_status": "unstable" if drift_count > 0 else "stable"
}

# 輸出結構
final_output = {
    "summary": summary,
    "drift_details": results
}

# 寫入結果
with open('version-monitoring-results.json', 'w', encoding='utf-8') as f:
    json.dump(final_output, f, ensure_ascii=False, indent=2)

# 即時輸出摘要
print("\n📊 版本監控總結：")
print(f"總語義單位數：{summary['total_nodes']}")
print(f"偵測到偏移警示：{drift_count} 次")
print(f"系統狀態：{summary['system_status']}")
print(f"\n📦 完整結果已輸出至 version-monitoring-results.json")
