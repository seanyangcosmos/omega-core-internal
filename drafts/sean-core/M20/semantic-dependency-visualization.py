import yaml
import networkx as nx
import matplotlib.pyplot as plt

# 載入語義鏈結構資料
with open('semantic-dependency-map.yaml', 'r', encoding='utf-8') as f:
    map_data = yaml.safe_load(f)

G = nx.DiGraph()

# 加入節點
for node in map_data['semantic_dependency_map']['nodes']:
    node_id = node['id']
    label = f"{node_id}\n({node['version']})"
    G.add_node(node_id, label=label)

# 加入依賴邊
for node in map_data['semantic_dependency_map']['nodes']:
    for dep in node.get('dependencies', []):
        G.add_edge(dep, node['id'], style='solid', color='black')

# 標記偏移警示邊
for warning in map_data['semantic_dependency_map'].get('drift_warnings', []):
    G.add_edge(warning['source'], warning['affected'], style='dashed', color='red')

# 生成佈局
pos = nx.spring_layout(G)

# 繪製節點
labels = nx.get_node_attributes(G, 'label')
nx.draw_networkx_nodes(G, pos, node_size=1500, node_color='lightblue')
nx.draw_networkx_labels(G, pos, labels, font_size=8)

# 區分邊類型繪製
solid_edges = [(u, v) for u, v, d in G.edges(data=True) if d['style'] == 'solid']
dashed_edges = [(u, v) for u, v, d in G.edges(data=True) if d['style'] == 'dashed']

nx.draw_networkx_edges(G, pos, edgelist=solid_edges, arrows=True, edge_color='black')
nx.draw_networkx_edges(G, pos, edgelist=dashed_edges, arrows=True, style='dashed', edge_color='red')

# 顯示圖形
plt.title("Semantic Dependency Map with Drift Warnings")
plt.axis('off')
plt.show()
