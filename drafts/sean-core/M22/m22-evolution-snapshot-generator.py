import json
import os
from datetime import datetime

# 假設來源資料為目前語義鏈演化結構
with open('evolution-tracking-results.json', 'r', encoding='utf-8') as f:
    evolution_data = json.load(f)

# 產生快照資料（實際可根據結構內容挑選重要部分）
snapshot = {
    "timestamp": datetime.now().isoformat(),
    "structure_snapshot": evolution_data,
    "notes": "自動生成語義鏈結構快照"
}

# 版本歷程資料檔案
history_path = 'evolution-version-history.json'
if os.path.exists(history_path):
    with open(history_path, 'r', encoding='utf-8') as f:
        history = json.load(f)
else:
    history = []

# 記錄新快照摘要
history.append({
    "version_id": f"v{len(history)+1}",
    "timestamp": snapshot['timestamp'],
    "summary": "語義鏈結構自動快照生成",
    "critical_mutations_detected": evolution_data['summary']['critical_mutations_detected']
})

# 輸出快照檔
snapshot_path = f"m22-evolution-snapshots/snapshot-v{len(history)}.json"
os.makedirs("m22-evolution-snapshots", exist_ok=True)

with open(snapshot_path, 'w', encoding='utf-8') as f:
    json.dump(snapshot, f, ensure_ascii=False, indent=2)

# 更新版本歷程
with open(history_path, 'w', encoding='utf-8') as f:
    json.dump(history, f, ensure_ascii=False, indent=2)

print(f"\n📦 語義鏈結構快照已生成：{snapshot_path}")
print(f"📜 版本歷程已更新：{history_path}")
