import pandas as pd
import csv
# 读取原始CSV文件路径
csv_file_path = 'D:\glossannotation\pythonProject1\dabaoyasuo\output_data.csv'

# 初始化一个空列表来存储每一行数据
data = []

# 打开CSV文件并逐行读取
with open(csv_file_path, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        # 检查行中是否包含正确数量的字段（假设应为2个字段）
        if len(row) >= 2:
            # 将多余的部分合并到第二个字段中
            key = row[0]
            value = ','.join(row[1:])
            data.append([key, value])
        else:
            print(f"Skipping malformed row: {row}")

# 将数据转换为DataFrame并添加表头
df = pd.DataFrame(data, columns=['Key', 'Value'])

# 保存带表头的文件
csv_file_with_header = './train.csv'
df.to_csv(csv_file_with_header, index=False)

print(f"已将表头添加到文件并保存为 {csv_file_with_header}")
