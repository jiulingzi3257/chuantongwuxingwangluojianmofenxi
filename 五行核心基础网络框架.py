import networkx as nx
from pyvis.network import networkx

#1.核心:五行节点
five_elements=["木","火","土","金","水"]

#2.基础关系边(用列表存储(起点,终点,关系边,权重))
base_edges=[
    #生关系
    ("木","火","生",1.0)
    ("火","土","生",1.0)
    ("土","金","生",1.0)
    ("金","水","生",1.0)
    ("水","木","生",1.0)
    #克关系
    ("木","土","克",-0.5)
    ("土","水","克",-0.5)
    ("水","火","克",-0.5)
    ("火","金","克",-0.5)
    ("金","木","克",-0.5)
    #泄关系(生关系的反向，属于弱干扰)
    ("火","木","泄",-0.8)
    ("土","火","泄",-0.8)
    ("金","土","泄",-0.8)
    ("水","金","泄",-0.8)
    ("木","水","泄",-0.8)
    #耗关系（克关系的反向，属于弱干扰）
    ("土","木","耗",-1.0)
    ("水","土","耗",-1.0)
    ("火","水","耗",-1.0)
    ("金","火","耗",-1.0)
    ("木","金","耗",-1.0)

]

#3.初始化有向图
G=nx.DiGraph()

#4.添加核心节点（可给节点加维度属性，比如核心节点标为“核心-五行”）
for elem in five_elements:
    G.add_node(elem,category="核心-五行",color="#FF6B6B")#节点颜色自定义
    #5.添加基础关系边:遍历列表(边的属性、关系类型、权重)
    for start,end,rel_type,weight in base_edges:
        #给不同关系边设不同颜色，方便区分
        edge_color="#4ECDC4"if weight>0 else"#FF9F43"
        G.add_edge(
            start,end,
            relationship=rel_type,
            weight=weight,
            color=edge_color,
            width=abs(weight)*2
        )

#6.动态可视化有向图（生成HTML文件，打开后可拖拽节点、hover看属性）
net=networkx(notebook=False,directed=True,height="800px",width="100%")
net.from_nx(G)

#调节节点标签显示（hover时显示“节点名+类别+边属性”）
for node in net.nodes:
    node["title"]=f"节点:﹛node['id']﹜\n类别:﹛node['category']﹜"
    for edge in net.edges:
        start=edge["from"]
        end=edge["to"]
        nx_edges=G.get_edge_data(start,end) #取同一对节点的所有边

        edge_attr=next(iter(nx_edges.values()))
        edge["title"]=f"关系:﹛edge_attr['relationship']﹜\n权重:﹛edge_attr['weight']﹜﹜"
        








