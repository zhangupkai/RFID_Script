import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from base_list import get_degree_list

# 相位随角度（9个固定角度）的变化

# tag1 = 'B034'
# tag2 = 'B029'

tag1 = 'B016'
tag2 = 'B023'

file_path = f'../tagPair/data/dataset/{tag1}_{tag2}/fixed_degree/{tag1}_{tag2}(1)(1).csv'
data = np.array(pd.read_csv(file_path, header=None))

# 只取f1=920.625的数据
phase_f1 = data[:, 0]

plt.title(f'Phase Orientation Time (Tag Pair {tag1}_{tag2})')
plt.plot(get_degree_list(), phase_f1, marker='o', markersize=3)
plt.show()
