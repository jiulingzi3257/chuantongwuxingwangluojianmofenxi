# -*- coding: utf-8 -*-
from docx import Document
doc = Document(r'C:\Users\85848\Doubao\chats\2026-09-30\new-chat\传统五行网络建模分析项目计划书_完善版.docx')

checks = [
    ('二维宽表703条目', '节点口径修正'),
    ('超291次下载', '下载量更新'),
    ('I Ching Graph Theory', '易图学译法'),
    ('数据状态诚实声明', '数据状态声明'),
    ('PNA/SNA双网络', 'PNA/SNA方法'),
    ('跨学科交叉超边', '超边方法'),
    ('双仓库策略', '双仓库说明'),
]

for keyword, label in checks:
    found = False
    for p in doc.paragraphs:
        if keyword in p.text:
            found = True
            break
    if not found:
        for table in doc.tables:
            for row in table.rows:
                for cell in row.cells:
                    if keyword in cell.text:
                        found = True
                        break
    status = 'OK' if found else 'MISSING'
    print(f'  [{status}] {label}')

# 风险表格
for table in doc.tables:
    first_row = ''.join([c.text for c in table.rows[0].cells])
    if '风险类型' in first_row:
        n = len(table.rows)
        last = ''.join([c.text for c in table.rows[-1].cells])
        print(f'  [INFO] 风险表格共{n}行')
        if '数据隐私' in last:
            print('  [OK] 数据隐私风险行已添加')
        break
