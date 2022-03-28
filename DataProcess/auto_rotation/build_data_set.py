import pandas as pd
import numpy as np
import os

# 遍历dataset，将文件地址和label存入csv

file_list = []
filepath = 'phase_mat_data'
for root, dir_names, filenames in os.walk(filepath):
    for filename in filenames:
        if filename == 'dataset.csv' or filename == 'testDataInfo.csv' or filename == 'trainDataInfo.csv':
            continue
        file_label = []
        file_list_str = os.path.join(root, filename)
        file_list_str = file_list_str.replace('\\', '/')
        file_label.append(file_list_str)
        if 'B016_B023' in filename:
            file_label.append(0)
        elif 'B016_AA03' in filename:
            file_label.append(1)
        elif 'B034_B029' in filename:
            file_label.append(2)
        file_list.append(file_label)
        print(file_label)

df = pd.DataFrame(data=file_list)
print(df)
df.to_csv(f'{filepath}/dataset.csv', index=False, header=False)
