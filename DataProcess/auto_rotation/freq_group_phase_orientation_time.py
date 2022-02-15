import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

# # 转动标签对，相位差随时间（角度）的变化，根据频率对数据进行分组

tag1 = 'B034'
tag2 = 'B029'

# tag1 = 'B016'
# tag2 = 'B023'

# tag1 = 'B016'
# tag2 = 'AA03'

count = 11
bath_dir = f'../../data/tagPair/auto_rotation/{tag1}_{tag2}/{tag1}_{tag2}({count})_25.0.csv'
df = pd.read_csv(bath_dir, header=None, names=['epc', 'freq', 'timestamp', 'phase', 'rssi'])

grouped = df.groupby('freq')

for name, group in grouped:
    print(name)
    print(group)
    save_path = f'../../data/tagPair/auto_rotation/{tag1}_{tag2}/{tag1}_{tag2}({count})_25.0_{name}.csv'
    np.savetxt(save_path, group, delimiter=',')
