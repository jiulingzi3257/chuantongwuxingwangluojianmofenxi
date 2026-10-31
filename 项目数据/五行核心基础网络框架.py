# -*- coding: utf-8 -*-
"""五行核心基础网络框架（最小骨架教学演示 / fixed skeleton demo）

相对线上旧版的四处修复（C-2）：
1. 边循环移出节点循环（原缩进在节点 for 内，20 条边被重复添加 5 次）；
2. f-string 全角花括号 ﹛﹜ 改为英文 {}（原写法不插值、原样字面输出）；
3. 边 hover 说明改为 add_edge 时直接写入；旧版 net.from_nx 之后用
   G.get_edge_data(start,end) 反查，get_edge_data 返回属性 dict，
   next(iter(...values())) 取到标量后再下标会 TypeError，且 from/to 方向可能错位；
4. pyvis 保存方法由不存在的 save_graph / 错误类名调用改为 write_html。

口径说明（边界，勿外推为已完成能力）：
- 本脚本用内置中文节点（木火土金水）与生克泄耗四类基础关系演示最小骨架；
- 与两个 .xlsx 数字 Id（0-4）的对齐、以及核心-边缘/小世界等拓扑结论，
  属于另一数据层与统计检验任务，不在本脚本修复范围；当前 5 节点 20 边骨架
  不构成核心-边缘或小世界的实证证据（见《骨架拓扑复算说明.md》）。

本轮渲染层修复（C-3，仅改可视化参数，节点与权重数据不变）：
1. Network 构造补 cdn_resources="in_line"：vis-network 9.1.2 的 css/js 内联进单 HTML，
   不再依赖会失效的外部 CDN（原默认 remote 分支引用的 cdnjs 资源含 SRI 校验，加载失败时画布空白）；
2. add_edge 的 arrows=True 改为 arrows="to"：vis-network 9.1.2 的 edges.arrows 只接受
   字符串或对象，布尔 true 会抛错并中断边渲染；
3. 四类关系权重与生克泄耗口径维持原样（生 +1.0、克 -0.5、泄 -0.8、耗 -1.0），本次未改动任何数据。
"""
import os
import networkx as nx
from pyvis.network import Network

# 1. 核心五行节点
five_elements = ["木", "火", "土", "金", "水"]

# 2. 基础关系边：(起点, 终点, 关系类型, 权重)
base_edges = [
    # 生关系 +1.0（传世出处见 edges 表 Label：《春秋繁露·五行相生》）
    ("木", "火", "生", 1.0),
    ("火", "土", "生", 1.0),
    ("土", "金", "生", 1.0),
    ("金", "水", "生", 1.0),
    ("水", "木", "生", 1.0),
    # 克关系 -0.5（传世出处见 edges 表 Label：《春秋繁露·五行相胜》）
    ("木", "土", "克", -0.5),
    ("土", "水", "克", -0.5),
    ("水", "火", "克", -0.5),
    ("火", "金", "克", -0.5),
    ("金", "木", "克", -0.5),
    # 泄关系 -0.8（传世原典出处待考，仅演示类型权重，不预支出处）
    ("火", "木", "泄", -0.8),
    ("土", "火", "泄", -0.8),
    ("金", "土", "泄", -0.8),
    ("水", "金", "泄", -0.8),
    ("木", "水", "泄", -0.8),
    # 耗关系 -1.0（传世原典出处待考，仅演示类型权重，不预支出处）
    ("土", "木", "耗", -1.0),
    ("水", "土", "耗", -1.0),
    ("火", "水", "耗", -1.0),
    ("金", "火", "耗", -1.0),
    ("木", "金", "耗", -1.0),
]

# 3. 初始化有向图（用于结构自检统计，不直接决定可视化属性）
G = nx.DiGraph()

# 4. 添加核心节点
for elem in five_elements:
    G.add_node(elem, category="核心-五行", color="#FF6B6B")

# 5. 添加基础关系边（顶层遍历，不嵌套在节点循环内）
for start, end, rel_type, weight in base_edges:
    edge_color = "#4ECDC4" if weight > 0 else "#FF9F43"
    G.add_edge(
        start, end,
        relationship=rel_type,
        weight=weight,
        color=edge_color,
        width=abs(weight) * 2,
    )

# 6. 动态可视化：pyvis 直接建图，边属性（含 hover 说明）在 add_edge 时写入，
#    不依赖 from_nx 之后对 net.edges 的反查（避免 from/to 与 nx 边方向错位）。
net = Network(notebook=False, directed=True, height="800px", width="100%",
              cdn_resources="in_line")

for elem in five_elements:
    net.add_node(
        elem, label=elem, size=30, color="#FF6B6B",
        title=f"节点: {elem}\n类别: 核心-五行",
    )

for start, end, rel_type, weight in base_edges:
    edge_color = "#4ECDC4" if weight > 0 else "#FF9F43"
    net.add_edge(
        start, end,
        title=f"关系: {rel_type}\n权重: {weight}",
        color=edge_color, width=abs(weight) * 2, arrows="to",
    )

# 7. 写出交互式 HTML（输出到脚本所在目录；vis-network 资源经 cdn_resources="in_line"
#    内联进单文件，无需联网加载外部 CDN；arrows 用字符串 "to"，为 vis-network 9.1.2 合法值）
out_dir = os.path.dirname(os.path.abspath(__file__))
out_path = os.path.join(out_dir, "五行核心基础网络框架.html")
net.write_html(out_path)

# 控制台自检输出：5 节点、20 边、四类各 5
kind_count = {}
for _, _, d in G.edges(data=True):
    kind_count[d["relationship"]] = kind_count.get(d["relationship"], 0) + 1
print(f"nodes={G.number_of_nodes()} edges={G.number_of_edges()}")
print("by_kind=", kind_count)
print("written=", out_path)









