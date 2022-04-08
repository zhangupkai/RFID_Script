import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import interpolate
from filters import hampel
from base_list import get_freq_list
from locate_degree_main import locate_degree
from cal_rotation_cycle_time_main import cal_rotation_cycle_time


rotation_level = 'auto_rotation_v4'
rotation_level_abbr = '_v4_combine_freq'

# tag1 = 'E002'
# tag2 = 'C001'

tag1 = 'E002'
tag2 = 'E006'
# count = 10

for count in range(31, 41):
    col = 0
    for freq in get_freq_list():
        bath_dir = f'phase_time_sequence/{rotation_level}/{tag1}_{tag2}({count})_{freq}.csv'
        data = np.array(pd.read_csv(bath_dir, header=None))
        timestamp = data[:, 0]
        phase = data[:, 1]
        # phase_timestamp = dict(zip(timestamp, phase))
        # size = timestamp.shape[0]

        # 去除异常值
        phase_after = hampel(phase)
        # 转动周期，微秒级
        # circle_time = cal_rotation_cycle_time(timestamp, phase_after, f'{tag1}_{tag2}')

        # 单个频率下，在相位角度时间序列中定位到指定的9个角度
        phase_orientation = locate_degree(timestamp, phase_after, f'{tag1}_{tag2}')

        # 最终得到的相位矩阵，9个角度（9行），8个频率（8列）
        phase_mat = np.zeros((9, 8))

        phase_mat[:, col] = np.array(phase_orientation)
        col += 1

    save_path = f'phase_mat_data/{tag1}_{tag2}/{tag1}_{tag2}{rotation_level_abbr}({count}).csv'
    np.savetxt(save_path, phase_mat, delimiter=',')
