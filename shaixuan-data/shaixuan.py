import pandas as pd
import ast

# 加载 Excel 文件
data = pd.read_excel(r'./test.xlsx')

# 将Value列中的字符串转换为字典
data['Value'] = data['Value'].apply(ast.literal_eval)

# 读取list2.txt中的已上传数据名称
with open('list2.txt', 'r') as file:
    uploaded_datasets = set(line.strip().split('/')[-1] for line in file.readlines())

# 简化data中的路径信息，并进行筛选
filtered_data = data[data['Value'].apply(lambda x: x['name'].split('/')[-1] in uploaded_datasets)]

# 可以选择打印或保存结果
print(filtered_data)
# 如果需要，可以将结果保存到新的Excel文件
filtered_data.to_excel('test_filtered_data.xlsx', index=False)
