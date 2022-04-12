import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from base_list import get_degree_list

# 相位随角度（9个固定角度）的变化

# tag1 = 'B034'
# tag2 = 'B029'

# tag1 = 'B016'
# tag2 = 'B023'

# tag1 = 'E002'
# tag2 = 'E006'

# tag1 = 'F001'
# tag2 = 'F005'

# tag1 = 'F001'
# tag2 = 'E006'

# tag1 = 'E002'
# tag2 = 'C001'

# tag1 = 'E004'
# tag2 = 'E005'

tag1 = 'C001'
tag2 = 'C002'

count_i = 3
count_j = 3

file_path = f'../tagPair/data/dataset/{tag1}_{tag2}/{tag1}_{tag2}({count_i})({count_j}).csv'
data = np.array(pd.read_csv(file_path, header=None))

for col in range(0, 8):
    # 只取f1=920.625的数据
    phase_f1 = data[:, col]

    plt.title(f'Phase Orientation Tag Pair {tag1}_{tag2}({count_i})({count_j})_f{col}')
    plt.plot(get_degree_list(), phase_f1, marker='o', markersize=3)
    plt.show()
