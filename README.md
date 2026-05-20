[五行核心基础网络框架.py](https://github.com/user-attachments/files/24835273/default.py)[五行核心基础网络框架.py](https://github.com/user-attachments/files/24835153/default.py)
[五行核心基础网络框架.py](https://github.com/user-attachments/files/24835164/default.py)


## 介绍:
这是一个用网络科学和python对中国传统五行以及传统罗盘进行网络建模分析的跨学科开源项目，其中，五行万物类象节点表，第一列为节点名称/类型/维度编号，第一行为标题，第二行为核心节点，部分复杂关系节点的多层属性已经用标点符号和空格分隔，是我基于邵雍的系统思维启发，已经按维度（天S、地D、人R）对关系节点进行编号和横向分布，除五个核心外，其余大部分关系节点均可能存在属性爆炸，鉴于此，咱们就先做一番基础网络验证，而后用pandas库创多层嵌套字典，接着咱们尝试用邵雍的八卦万物类象做完本地预演，最后，各位还可接入AI模型API进行训练。
核心目标是通过Python量化建模，解构传统五行万物类象、罗盘方位体系的复杂关系网络，验证其系统关联性，并提供从基础网络分析到AI模型接入的全流程实操方案。

**This project builds a dynamic network model of the Zhouyi (Yijing, 易经) system based on network science, aiming to deconstruct the native logic of Chinese Axial Age philosophy. The modeling framework extends beyond the Zhouyi to encompass the broader categorical correspondence systems (wanwu leixiang, 万物类象) of the Wuxing (五行, Five Phases) and compass traditions.**
**本项目基于网络科学构建了《周易》（《易经》）系统的动态网络模型，旨在解构中国轴心时代哲学的内在逻辑。该建模框架不仅限于《周易》，还涵盖了五行（五行，Five Phases）和指南针传统中更广泛的分类对应系统（万物类象，wanwu leixiang）.**

**Peers from digital humanities, network science, Sinology, and philosophy are warmly welcomed to contribute suggestions, critiques, or collaborations.**
**我们热烈欢迎来自数字人文、网络科学、汉学和哲学领域的同行提出建议、批评或合作。**

## 核心特色
1. **跨学科融合**：网络科学方法论 + 传统五行/罗盘体系 + Python数据工程； 
2. **分层节点设计**：核心节点（五行：金木水火土）+ 多层属性节点（万物类象），通过标点/空格分隔复杂属性，适配网络建模；
3. **渐进式实操路径**：从基础网络验证 → 多层嵌套字典构建 → 八卦万物类象预演 → AI模型API接入
4. 支持调整关系边权重、拓展关系节点，接入不同AI模型训练。

## 数据目录
[五行万物类象表-3b874189 (2).xlsx](https://github.com/user-attachments/files/24835189/-3b874189.2.xlsx)

[八卦万物类象.docx](https://github.com/user-attachments/files/24271622/default.docx)

## 节点、关系数据来源：
萧吉《五行大义》、《尚书·洪范》、《黄帝内经》、《渊海子平》、《子平真诠》、《千里命稿》、《奇门遁甲元灵经》、《奇门遁甲秘笈大全》等


## 核心数据说明
### 五行万物类象节点表（wuxing_nodes.csv）
- 第一列：节点名称/类型/维度编号（格式：`节点名_类型_维度编号`，如`木_自然属性_S10`，S=天、D=地、R=人）；
- 首行：列标题（核心节点/属性维度/关联权重）；
- 第二行：五行核心节点（金/木/水/火/土）；
- 复杂属性：通过标点（）和、和空格分隔多层属性，适配嵌套字典构建；
-「属性爆炸」处理：优先验证核心节点关联，再通过pandas构建多层嵌套字典逐层拓展关系节点属性。
### 基础关系边权重表
目前只提供了生克泄耗那20条最基础的关系边权重：如木生火生土生金生水，水生木;水克火，火克金，金克木，木克土，土克水。
其余隐藏关系边需通过社区发现最短路径跨文本计量算法挖掘。




## 2. 核心流程实操
    快速开始：
步骤 1：基础网络验证，初步验证五行节点的基础拓扑关系：
python -m pip install networkx pyvis pandas openpyxl openai numpy
[五行核心基础网络框架.py](https://github.com/user-attachments/files/24835386/default.py)


后续计划：
步骤 2：构建多层嵌套字典
基于pandas解析节点表，生成适配网络分析的多层嵌套字典（按维度 - 节点 - 属性分层）
步骤 3：利用邵雍八卦万物类象进行本地预演：
安装准备：pip install scikit-learn python-lovain
步骤 4：接入AI模型：
开发建议：
可借用doubao-seed-1-6-thinking-250615、doubao-pro-32k
调用API示例：
从 volcenginesdkarkruntime 导入 Ark
client = Ark(api_key="你的_api_key")

= client.chat.completions.create( model="your_endpoint_id", messages=[{"role": "user", "content": "分析网络拓扑结构..."}] )

## 项目依赖：
数据处理	pandas、numpy
网络建模	networkx
可视化	matplotlib（可自选）、seaborn（可自选）、pyvis
深度学习：	DGL、PyTorch Geometric（可自选）
全网检索与对接：requests、openai-python  （可自选）  
古汉语大模型-AI太炎

知乎开放数据平台：https://developer.zhihu.com
DeepSeek开放数据平台：https://platform.deepseek.com/usage

火山引擎开放数据平台：http://volcengine.com/product/doubao

火山引擎开放数据平台相关APU文档：http://api.volcengine.com/api-docs/view?action=AddGraphTables&version=2025-08-15&serviceCode=graph

国内学术，想深入了解者请走镜像：https://gitee.com/intellectualdisability-of-jun-sen/chuantongwuxingwangluojianmofenxi


**欢迎各位同行提出建议、交流协作。国际同行可通过 GitHub Issues 提交英文反馈，我会以中文+简短英文回复。**
**International peers are welcome to submit feedback, bug reports, or collaboration inquiries via GitHub Issues. I will respond in English or bilingual format. For longer discussions related to classical text exegesis or network modeling methodology, feel free to reference the relevant literature nodes and edge tables in the data/ directory.**

   









