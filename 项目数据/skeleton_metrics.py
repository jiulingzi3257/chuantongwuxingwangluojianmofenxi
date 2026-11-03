# -*- coding: utf-8 -*-
"""
五行最小骨架（5 节点 / 20 边）拓扑指标复算 —— 检修清单 7.5 落地脚本
只读两个本地 xlsx，不写回仓库、不联网。
口径：描述性统计；n=5 极小样本，不构成小世界 / 核心-边缘证明。
"""
import os, sys, re, json
from collections import defaultdict
import openpyxl
import networkx as nx

sys.stdout.reconfigure(encoding="utf-8")

# 数据路径优先级：① 命令行参数 ② 与脚本同目录的两表（入库后可直接复跑）
# ③ 本机旧稿绝对路径回退（仅作者本机复跑用，他人环境不存在则报清晰错误）
HERE = os.path.dirname(os.path.abspath(__file__))
_FB_NODES = r"C:\Users\85848\OneDrive\文档\1628091051\五行基础模型-万物nodes.xlsx"
_FB_EDGES = r"C:\Users\85848\OneDrive\文档\1628091051\五行基础模型edges类象关系表.xlsx"

def _pick(arg, rel_name, fallback):
    if arg:
        return arg
    rel = os.path.join(HERE, rel_name)
    return rel if os.path.exists(rel) else fallback

NODES = _pick(sys.argv[1] if len(sys.argv) > 1 else None,
              "五行基础模型-万物nodes.xlsx", _FB_NODES)
EDGES = _pick(sys.argv[2] if len(sys.argv) > 2 else None,
              "五行基础模型edges类象关系表.xlsx", _FB_EDGES)
for p in (NODES, EDGES):
    if not os.path.exists(p):
        sys.exit(f"[缺失] 找不到数据表：{p}\n请用 `python skeleton_metrics.py <nodes.xlsx> <edges.xlsx>` 指定路径。")

def load_table(path, sheet=None):
    wb = openpyxl.load_workbook(path, data_only=True)
    ws = wb[sheet] if sheet else wb.active
    rows = list(ws.iter_rows(values_only=True))
    header = [str(c).strip() if c is not None else "" for c in rows[0]]
    data = [dict(zip(header, r)) for r in rows[1:] if any(c is not None for c in r)]
    return header, data

# ---------- 1. 原始数据核对 ----------
nh, nodes = load_table(NODES)
eh, edges = load_table(EDGES)
print("== NODES header ==", nh)
print("== EDGES header ==", eh)
print(f"节点数={len(nodes)}  边数={len(edges)}")

def classify(label, kind, typ):
    s = f"{label or ''} {kind or ''} {typ or ''}"
    if "相生" in s: return "相生"
    if "相胜" in s or "相克" in s: return "相克"
    if "相泄" in s: return "相泄"
    if "相耗" in s: return "相耗"
    return "未分类"

cat_count = defaultdict(int)
cat_weight = defaultdict(float)
edge_rows = []
for e in edges:
    src = e.get("Source"); tgt = e.get("Target")
    w = e.get("Weight"); w = float(w) if w is not None else 0.0
    cat = classify(e.get("Label"), e.get("Kind"), e.get("Type"))
    cat_count[cat] += 1
    cat_weight[cat] += w
    edge_rows.append((src, tgt, cat, w, e.get("Id"), e.get("Label")))

print("\n== 四类边计数 / 权重和 ==")
for c in ["相生", "相克", "相泄", "相耗", "未分类"]:
    if cat_count[c]:
        print(f"{c}: {cat_count[c]} 条, 权重和={round(cat_weight[c],3)}")

print("\n== 全部边明细 (Source,Target,类别,Weight,Id,Label) ==")
for r in edge_rows:
    print(r)

# ---------- 2. 构图 ----------
DG = nx.DiGraph()
for n in nodes:
    nid = n.get("Id")
    DG.add_node(nid, label=n.get("Label"), core=n.get("Iswuxingcore"),
                wl=n.get("wuxing label"), wid=n.get("wuxing Id"), dim=n.get("维度"))
for src, tgt, cat, w, eid, label in edge_rows:
    DG.add_edge(src, tgt, weight=w, cat=cat, eid=eid, label=label)

UG = nx.Graph()
for n, d in DG.nodes(data=True): UG.add_node(n, **d)
for u, v, d in DG.edges(data=True):
    if UG.has_edge(u, v):
        UG[u][v]["weight"] += d["weight"]
        UG[u][v]["cats"] = UG[u][v].get("cats", []) + [d["cat"]]
    else:
        UG.add_edge(u, v, weight=d["weight"], cats=[d["cat"]])

# ---------- 3. 结构指标 ----------
print("\n== 结构指标 ==")
print("节点数 n =", DG.number_of_nodes())
print("有向边数 m =", DG.number_of_edges())
print("无向投影边数 =", UG.number_of_edges())
weak = list(nx.weakly_connected_components(DG))
print("弱连通分量数 =", len(weak), " 各分量 =", [sorted(c) for c in weak])
strong = list(nx.strongly_connected_components(DG))
print("强连通分量数 =", len(strong), " 各分量 =", [sorted(c) for c in strong])

print("\n== 节点度 / 加权度（负权重=克泄耗方向） ==")
print(f"{'节点':<4}{'入度':>4}{'出度':>4}{'总度':>4}{'正权重和':>9}{'负权重和':>9}{'加权总度':>9}")
for nid in sorted(DG.nodes):
    indeg = DG.in_degree(nid); outdeg = DG.out_degree(nid)
    pos = sum(d["weight"] for _, _, d in DG.in_edges(nid, data=True) if d["weight"] > 0)
    pos += sum(d["weight"] for _, _, d in DG.out_edges(nid, data=True) if d["weight"] > 0)
    neg = sum(d["weight"] for _, _, d in DG.in_edges(nid, data=True) if d["weight"] < 0)
    neg += sum(d["weight"] for _, _, d in DG.out_edges(nid, data=True) if d["weight"] < 0)
    tot = pos + neg
    print(f"{nid:<4}{indeg:>4}{outdeg:>4}{indeg+outdeg:>4}{round(pos,2):>9}{round(neg,2):>9}{round(tot,2):>9}")

# 聚类系数（无向投影）
try:
    avg_clust = nx.average_clustering(UG)
    print("\n无向投影平均聚类系数 =", round(avg_clust, 4))
    trans = nx.transitivity(UG)
    print("传递性 transitivity =", round(trans, 4))
except Exception as ex:
    print("聚类系数计算异常:", ex)

# 平均最短路径（有向，仅弱连通分量内可达对）
for comp in weak:
    sub = DG.subgraph(comp)
    if sub.number_of_nodes() > 1:
        try:
            apl = nx.average_shortest_path_length(sub)
            print(f"分量 {sorted(comp)} 有向平均最短路径长度 = {round(apl,4)}")
        except nx.NetworkXError as ex:
            print(f"分量 {sorted(comp)} 不可达对存在，无法直接算有向 APL：{ex}")
        ug_sub = UG.subgraph(comp)
        if nx.is_connected(ug_sub):
            print(f"分量 {sorted(comp)} 无向平均最短路径长度 = {round(nx.average_shortest_path_length(ug_sub),4)}")

# 度分布
print("\n== 度分布（总度） ==")
dist = defaultdict(int)
for nid in DG.nodes:
    dist[DG.in_degree(nid) + DG.out_degree(nid)] += 1
print(dict(sorted(dist.items())))

# 悬空 / 孤立节点检查
isolated = [n for n in DG.nodes if DG.degree(n) == 0]
print("孤立节点 =", isolated)
# 边端点是否都在节点表
node_ids = {n.get("Id") for n in nodes}
orphan = [(s,t) for s,t,_,_,_,_ in edge_rows if s not in node_ids or t not in node_ids]
print("悬空边（端点不在节点表） =", orphan)

# ---------- 4. 正则性 / 完全图判定（解释聚类=1.0、APL=1.0 的成因） ----------
n = UG.number_of_nodes()
full_edges = n * (n - 1) // 2
print("\n== 完全图 / 正则性判定 ==")
print(f"无向投影节点 n={n}, 无向边={UG.number_of_edges()}, 完全图应有边 C(n,2)={full_edges}, 是否完全图={UG.number_of_edges()==full_edges}")
print("无向度序列 =", sorted(d for _, d in UG.degree()))
print("有向总度序列 =", sorted(DG.in_degree(x) + DG.out_degree(x) for x in DG.nodes))
# 度是否全部相等（正则图）
deg_values = [DG.in_degree(x) + DG.out_degree(x) for x in DG.nodes]
print("有向总度是否全相等（正则） =", len(set(deg_values)) == 1)
# 每类边是否构成一个有向环（5 阶循环）
print("\n== 各类边邻接序列（确认环结构） ==")
for c in ["相生", "相克", "相泄", "相耗"]:
    succ = {s: t for s, t, cat, *_ in edge_rows if cat == c}
    order = []
    cur = min(succ)
    for _ in range(len(succ)):
        order.append(cur); cur = succ[cur]
    print(f"{c}: {' -> '.join(map(str, order))} -> {succ.get(order[0]) if False else order[0]}")
