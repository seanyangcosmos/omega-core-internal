import json
import networkx as nx
import matplotlib.pyplot as plt

# 載入最新快照資料
with open('m22-evolution-snapshots/snapshot-v1.json', 'r', encoding='utf-8') as f:
    snapshot = json.load(f)

# 假設結構摘要內含語義單位與依賴關係（示意）
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

# 定義顏色
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
plt.title("語義鏈結構快照視覺化")
plt.show()
