import gzip
import pickle
import pandas as pd

def load_dataset_file(filename):
    with gzip.open(filename, "rb") as f:
        loaded_object = pickle.load(f)
        return loaded_object

# 指定您的数据文件路径
dev_label_path = 'labels.dev'

# 调用函数加载数据
dev_data = load_dataset_file(dev_label_path)

# 创建一个DataFrame
df = pd.DataFrame(list(dev_data.items()), columns=['Key', 'Value'])

# 指定输出Excel文件的路径
output_excel_path = 'dev_data.xlsx'

# 将DataFrame写入Excel文件
df.to_excel(output_excel_path, index=False)

print(f"数据已经被写入到 {output_excel_path}")
