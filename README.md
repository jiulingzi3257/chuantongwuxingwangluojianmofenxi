[五行核心基础网络框架.py](https://github.com/user-attachments/files/24835273/default.py)[五行核心基础网络框架.py](https://github.com/user-attachments/files/24835153/default.py)
[五行核心基础网络框架.py](https://github.com/user-attachments/files/24835164/default.py)

### 语言说明 / Language Note
**本仓库文档主体为简体中文（方便国内用户阅读），关键声明、核心术语均提供中英双语对照，符合数字人文领域国际协作规范。**
**The main body of the read file in this repository is in Simplified Chinese (for ease of reading by domestic users), with key statements and core terms provided in both Chinese and English, in accordance with international collaboration norms in the field of digital humanities.**

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
隋·萧吉《五行大义》、《尚书·周书·洪范》、先秦·汉佚名《黄帝内经》//《素问》//《金匮真言论》《阴阳应象大论》、《灵兰秘典论》、《六节藏象论》《五藏生》《五藏别论》《经脉别论》《脏气法时论》《宣明五气论》《玉机真藏论》《天元纪大论》《五运行大论》《气交变大论》《至真要大论》//《灵枢·本神》《经脉》等

汉·董仲舒《春秋繁露》//《卷十·五行对》//《卷十一·第四十二五行之义》//《卷十三·五行相生·五行相胜·五行顺逆·治水五行》//《卷十四·治乱五行·五行变数·五行五事》
## 2.命理术数-原生态本土五行人格理论雏形-关系节点、加权关系边数据：
郑同《御定子平》

宋·徐子平、徐升《渊海子平》

清·沈孝瞻《子平真诠》

清·雷明夏《子平管见》

明·张楠《神峰通考》

民国·韦千里《千里命稿》

宋·京图《滴天髓》

清·任铁樵《滴天髓·阐微》

民国·袁树珊《命理探原》

明·廖中《五行精纪》

辽·耶律淳《星命总括》

清·佚名《星平会海》

清·余春台《穷通宝鉴》

明·万民英《三命通会》

清·隐溪居士《奇门遁甲元灵经》

三国·蜀·诸葛亮《奇门遁甲统宗大全》 《奇门遁甲秘笈大全》

清·野鹤老人《增删卜易》（六爻方面对关系边权重的看法）等多部碎片化古籍。
## 核心数据说明
### 五行万物类象节点表（wuxing_nodes.csv）
- 第一列：节点名称/类型/维度编号（格式：`节点名_类型_维度编号`，如`木_自然属性_S10`，S=天、D=地、R=人）；
  
- 首行：列标题（核心节点/属性维度/关联权重）；
  
- 第二行：五行核心节点（金/木/水/火/土）；
  
- 复杂属性：通过标点（）和、和空格分隔多层属性，适配嵌套字典构建；

-「属性爆炸」处理：优先验证核心节点关联，再通过pandas构建多层嵌套字典逐层拓展关系节点属性。
### 基础关系边权重表
目前只提供了生克泄耗那20条最基础的关系边权重：如木生火、火生土、土生金、金生水、水生木;水克火，火克金，金克木，木克土，土克水。
其余隐藏关系边需通过社区发现最短路径、跨文本计量算法挖掘。

### 七、 核心发现与待实证的假设：
在对传统五行理论进行系统梳理时，发现 **传统五行是一张核心边缘多层属性动态网络** ，那核心边缘结构是否属实？ 


该理论发现核心价值可从四个层面入手： 一、范式价值：从“还原论”到“系统论”的跨越

过去两千年，五行主要被当作哲学概念或占卜工具，长期被还原论思维排斥在科学话语之外。我这个的发现首次证明：**五行不是五个孤立的标签，而是一个具有明确拓扑结构（核心-边缘）、关系边权重（生克泄耗）、多层属性（S/D/R）和动态演化规律（时序网络）的复杂系统**。是一个**中国传统五节点20条基础生克加权有向边五次幂的核心边缘结构多层属性嵌套动态关系模型**，这为“系统思维”“古系统思维”提供了一个可计算、可验证的古代范本，打破了“东方智慧只能定性、不能定量”的刻板印象。

二、网络科学价值：一个古老的“小世界”与“异质网络”案例

现代网络科学通常研究社交网络、生物网络、互联网等。我这个的发现揭示：中国先哲早在轴心时代就构建了一个具有**高聚类系数（同类象紧密连接）**和**短平均路径**（**任意节点约3步可达**）的“小世界网络”。 这为网络科学提供了一个非西方的、独立起源的经典案例，有助于检验网络演化模型的普适性。**同时，天、地、人三维节点的异质性分布，也为“多层网络”和“异质信息网络”研究提供了天然的数据集。**

三、方法论价值：为古籍活化提供“知识结构化”的元框架

当前古籍数字化多停留在影像扫描和文本标引层面，缺乏对知识内在逻辑的建模。我的节点表和关系边初始权重，虽然尚未数据清洗，可**首次将五行类象转化为可机器读取的“本体”（Ontology），为后续知识图谱构建、AI训练、跨文本挖掘提供了标准化的数据底座**。这直接回应了**国家“十五五”规划对“知识结构化”古籍数字化**的战略需求。

**四、跨学科价值：连接人文、社科与自然科学的桥梁**

· 本土心理学：我基于本次将五行的建模，回归其作为“**关系模型**”本质，对其本土人格研究中“**五行人格理论**”的扩展与延伸，为中医五态人格、大五人格等提供了动态演化的计算框架，可以开发比九型人格更具文化根基的人格测评工具。 
· 复杂系统医学：基于“五脏-五志-五气”的对应关系，可以辅助构建“情志致病”的藏象学说小世界网络的动力学机制，有助于在2025年中华医道大会之后辅助探索**心身疾病**的**非线性**网络动力学机制。

· AI可解释性：我的节点表为大语言模型理解中华传统概念（如“仁—木—肝—怒”）提供了结构化的语义锚点，有助于减少AI的“幻觉”和偏见。 
更具体落地方向等请参考主仓库的项目数据文件夹内模拟网络建模分析数据。


## 2. 核心流程实操
快速开始：
步骤 1：基础网络验证，初步验证五行节点的基础拓扑关系：

      python -m pip install networkx pyvis pandas openpyxl openai numpy
      
[五行核心基础网络框架.py](https://github.com/user-attachments/files/24835386/default.py)


后续计划：
Subsequent Plans

步骤 2：构建多层嵌套字典
Step 2: Construct multi-level nested dictionaries

Parse the node table based on pandas to generate multi-level nested dictionaries adapted for network analysis (layered by dimension-node-attribute).
基于pandas解析节点表，生成适配网络分析的多层嵌套字典（按维度 - 节点 - 属性分层）

步骤 3：利用邵雍八卦万物类象进行本地预演：
Step 3: Conduct local pre-simulation by applying Shao Yong's Eight Trigrams analogous in appearance of All Things:

Preparation for installing Python libraries:
安装准备：
      
      pip install scikit-learn python-lovain

步骤 4：接入AI模型：
Step 4: Integrate AI model
开发建议：
Development suggestions:

可借用doubao-seed-1-6-thinking-250615、doubao-pro-32k大模型
Borrowable doubao-seed-1-6-thinking-250615、doubao-pro-32k large model

调用API示例(python)：
Example of calling APU:

     pip install volcenginesdkarkruntime

official example:
官方示例：

     form volcenginesdkarkruntime import Ark
     client = Ark(api_key="your_api_key")= client.chat.completions.create( model="your_endpoint_id", messages=[{"role": "user", "content": "分析网络拓扑结构..."}] )

 完整版:
**Example of calling APU in the full version:**

    # 1. 导入依赖库
    from volcenginesdkarkruntime import Ark
    from volcenginesdkarkruntime.errors import ArkError
    import json  # 可选：若需要结构化输出时使用
    # 2. 初始化Ark客户端（核心配置）
    def init_ark_client(api_key: str):
    初始化Ark客户端
    try:
        client = Ark(api_key=api_key)
        return client
    except Exception as e:
        print(f"客户端初始化失败：{str(e)}")
        return None
    # 3. 构造拓扑分析的Prompt（结合你的预处理结果）
    def build_topology_analysis_prompt():
    """
    结合节点表清洗、社区发现/随机森林/决策树预演结果，构造精准Prompt
    （请根据实际数据替换示例中的占位符内容）
    """
    # 示例：预处理后的关键信息（你实际的节点/算法结果）
    preprocess_info = {
        "节点表维度": ["维度编号", "关系节点名", "属性列1", "属性列2"],
        "社区发现结果": "共识别出3个核心社区，社区1包含节点A/B/C，社区2包含节点D/E...",
        "随机森林预演结论": "节点属性X对拓扑连接权重的特征重要性达0.85",
        "决策树预演结论": "节点关系判定的核心分裂条件为属性Y>0.7"
    }
    # 构造用户指令（明确分析目标）
    prompt = f"""
    基于以下预处理后的网络拓扑数据和本地算法预演结果，完成以下分析：
    1. 预处理信息：{json.dumps(preprocess_info, ensure_ascii=False, indent=2)}
    2. 分析要求：
       - 解读社区发现结果对应的拓扑结构特征；
       - 结合随机森林的特征重要性，分析节点属性对拓扑连接的影响；
       - 基于决策树结论，给出拓扑关系判定的简化规则；
       - 总结该网络拓扑的核心特点和潜在优化方向。
    """
    return prompt
    # 4. 核心调用逻辑
    def analyze_network_topology(api_key: str, endpoint_id: str):
    """调用Ark API分析网络拓扑结构"""
    # 初始化客户端
    client = init_ark_client(api_key)
    if not client:
        return
    # 构造请求消息
    messages = [
        {"role": "user", "content": build_topology_analysis_prompt()}
    ]
    
    try:
        # 调用Chat Completions API
        response = client.chat.completions.create(
            model=endpoint_id,  # 你的方舟模型端点ID
            messages=messages,
            temperature=0.3,   # 低随机性，保证分析结果稳定
            max_tokens=2000     # 按需调整输出长度
        )
        
        # 解析响应结果
        analysis_result = response.choices[0].message.content
        print("=== 网络拓扑分析结果 ===")
        print(analysis_result)
        return analysis_result
    
    except ArkError as e:
        # 捕获方舟API专属异常
        print(f"API调用失败（ArkError）：错误码={e.code}，错误信息={e.message}")
    except Exception as e:
        # 捕获其他通用异常
        print(f"API调用异常：{str(e)}")
    # 5. 执行调用（替换为你的实际配置）
    if __name__ == "__main__":
    # 替换为你的真实API Key和Endpoint ID（火山方舟控制台获取）
    YOUR_API_KEY = "your_api_key"
    YOUR_ENDPOINT_ID = "your_endpoint_id"
    # 执行分析
    analyze_network_topology(YOUR_API_KEY, YOUR_ENDPOINT_ID)

## 二、关键说明
1.  配置替换： **your_api_key**：从火山引擎方舟控制台获取的 API 密钥（注意保密，不要硬编码到代码仓库）；**your_endpoint_id**：你部署的模型端点 ID（需先在方舟控制台完成模型部署）。
2. Prompt 优化： 示例中**preprocess_info**是占位符，需替换为你实际清洗后的节点表、社区发现 / 随机森林 / 决策树的输出结果；  分析要求可根据需求调整（比如增加「拓扑漏洞分析」「节点重要性排序」等）。
3. 工程化建议： ◦ API Key 建议通过环境变量注入（而非硬编码），例如**os.getenv("ARK_API_KEY")**； ◦ 若节点表数据量较大，可先提炼核心结论（而非全量传入），避免 Prompt 过长； 可增加响应结果的持久化（如写入文件 / 数据库），方便后续复用。
4. 异常处理： 代码中捕获了ArkError（方舟 API 专属异常）和通用异常，可根据实际需求扩展错误重试、告警等逻辑。
## 三、扩展场景（可选）
如果需要将本地预处理的节点表数据（CSV/Excel）直接传入 API，可在**preprocess_info**中补充数据样例（或文件链接），例如：
    
    import pandas as pd
    node_df = pd.read_csv("清洗后的节点表.csv")
    preprocess_info["节点表样例"] = node_df.head(10).to_dict(orient="records")  # 传入前10行样例

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

国内学术，核心资料，想深入了解者请走主仓库镜像：https://gitee.com/intellectualdisability-of-jun-sen/chuantongwuxingwangluojianmofenxi


**欢迎各位同行提出建议、交流协作。国际同行可通过 GitHub Issues 提交英文反馈，我会以中文+简短英文回复。**
**International peers are welcome to submit feedback, bug reports, or collaboration inquiries via GitHub Issues. I will respond in English or bilingual format. For longer discussions related to classical text exegesis or network modeling methodology, feel free to reference the relevant literature nodes and edge tables in the data/ directory.Or conduct in-depth discussions through GitHub discussion**

### 开源协议 / Open Source License

**This project is open-sourced under the [CC0-1.0 Open Source License], and you are free to use, modify, and distribute the resources of this project in accordance with the terms of the license.**
**本项目采用 [CC0-1.0开源协议] 开源，您可遵循协议条款自由使用、修改和分发本项目资源。**








