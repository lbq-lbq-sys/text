
import os
import pandas as pd

# 定义文件夹路径和输出文件路径
folder_path = r'D:\工行'
output_file = r'D:\工行\的表.csv'

# 获取文件夹中的所有 CSV 文件
files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

# 初始化一个空的 DataFrame 用于存储合并后的数据
combined_df = pd.DataFrame()

# 遍历所有文件并合并
for file in files:
    file_path = os.path.join(folder_path, file)
    try:
        # 尝试使用 utf-8 编码读取文件
        df = pd.read_csv(file_path, encoding='utf-8')
    except UnicodeDecodeError:
        # 如果 utf-8 失败，尝试使用 gbk 编码
        df = pd.read_csv(file_path, encoding='gbk')
    combined_df = pd.concat([combined_df, df], ignore_index=True)

# 将合并后的数据保存为 CSV 文件
combined_df.to_csv(output_file, index=False, encoding='utf-8-sig')

print(f"合并完成，文件已保存到 {output_file}")

