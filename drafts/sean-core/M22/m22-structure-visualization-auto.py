import json
import networkx as nx
import matplotlib.pyplot as plt
import os

# 自動偵測最新快照
snapshot_dir = 'm22-evolution-snapshots'
snapshots = sorted([f for f in os.listdir(snapshot_dir) if f.startswith('snapshot-v')])
latest_snapshot = snapshots[-1]

print(f"自動載入最新快照：{latest_snapshot}")

with open(os.path.join(snapshot_dir, latest_snapshot), 'r', encoding='utf-8') as f:
    snapshot = json.load(f)

# 假設結構資料來源與先前範例相同（結構內容請依實際快照調整）
structure = [
    {"id": "SC7", "type": "stable"},
    {"id": "SC7.2", "type": "mutation"},
    {"id": "SC7.3", "type": "extension"},
    {"id": "NEW-X", "type": "new"},
    {"id": "STB-2", "type": "stable"},
    {"id": "STB-3", "type": "orphan"}
]

dependencies = [
    ("SC7", "SC7.2"),
    ("SC7.2", "SC7.3"),
    ("SC7", "STB-2"),
    ("SC7", "NEW-X")
]

# 建構圖形
G = nx.DiGraph()

for node in structure:
    G.add_node(node['id'], status=node['type'])

for src, tgt in dependencies:
    G.add_edge(src, tgt)

# 顏色設定
color_map = []
for node in G:
    status = G.nodes[node]['status']
    if status == "stable":
        color_map.append('green')
    elif status == "mutation":
        color_map.append('red')
    elif status == "extension":
        color_map.append('blue')
    elif status == "new":
        color_map.append('orange')
    elif status == "orphan":
        color_map.append('gray')
    else:
        color_map.append('black')

# 畫圖
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color=color_map, node_size=800, arrows=True)
plt.title(f"語義鏈結構快照視覺化 - {latest_snapshot}")
plt.show()
