import pandas as pd

file_path = r'D:\银行查询\directory.csv'
df = pd.read_csv(file_path)

# 修改: 添加 errors='ignore' 参数以忽略无法编码的字符
df.to_csv(r'D:\Users\cn.csv', encoding='gbk', errors='ignore')
df1= df[df['City']=='成都市']
df1.to_csv(r'D:\Users\cd.csv', encoding='gbk', errors='ignore')
print(df1)

# 或者修改: 将编码改为 utf-8 以支持更广泛的字符集
# df.to_csv(r'D:\Users\cn.csv', encoding='utf-8')