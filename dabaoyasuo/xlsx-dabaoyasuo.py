import pandas as pd

# 读取Excel文件
xlsx_file_path = './train_filtered_data.xlsx'
data = pd.read_excel(xlsx_file_path)

# 检查数据
print(data.head())

# 保存为CSV文件，确保编码为utf-8，这可以处理大多数语言的字符
csv_file_with_header = './test_filtered_data.csv'
data.to_csv(csv_file_with_header, index=False, encoding='utf-8')

print(f"已将表头添加到文件并保存为 {csv_file_with_header}")
