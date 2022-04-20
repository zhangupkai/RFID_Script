import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import interpolate
from filters import hampel
from base_list import get_freq_list
from locate_degree_main import locate_degree
from cal_rotation_cycle_time_main import cal_rotation_cycle_time

"""
转动标签对，相位差随时间（角度）的变化
Group1.3  8个不同频率下的数据 
"""

# tag1 = 'E002'
# tag2 = 'C001'

# tag1 = 'E002'
# tag2 = 'E006'

# tag1 = 'F001'
# tag2 = 'F005'

# tag1 = 'F001'
# tag2 = 'E006'

tag1 = 'E004'
tag2 = 'E005'

# tag1 = 'C001'
# tag2 = 'C002'

# tag1 = 'C003'
# tag2 = 'C004'

# tag1 = 'F002'
# tag2 = 'F003'

# rotation_level = 'final_experiment/1_hop'
# rotation_level = 'final_experiment/2_rotation_level/level_3'
# rotation_level = 'final_experiment/3_object_distance/distance_3'
# rotation_level = 'final_experiment/5_tag_type/type_1'
rotation_level = 'final_experiment/6_interfer_tag_numbers/interfer_2'
# rotation_level = 'final_experiment/7_object_material/material_2'
rotation_level_abbr = '_c6.2'

is_expand_dataset = True

# 为了扩充数据集，交叉互换不同组数据中的频率，swap_freq表示需要互换的频率
# swap_freq_count = 0
# swap_freq = get_freq_list()[swap_freq_count]
# print(f'swap freq is f{swap_freq_count}: {swap_freq}')

if is_expand_dataset:
    # swap_freq_count = 0
    # for swap_freq in get_freq_list()[0:4]:
    swap_freq_count = 4
    for swap_freq in get_freq_list()[4:8]:
        print(f'swap freq is f{swap_freq_count}: {swap_freq}')

        # for count_i in range(24, 26):
        #     for count_j in range(24, 26):
        for count_i in range(26, 28):
            for count_j in range(26, 28):
                if count_j == count_i:
                    continue

                # 最终得到的相位矩阵，9个角度（9行），8个频率（8列）
                phase_mat = np.zeros((9, 8))

                col = 0
                # 上一轮循环中的phase_orientation
                pre_phase_orientation = []
                for freq in get_freq_list():
                    count = count_i
                    if freq == swap_freq:
                        count = count_j

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
                    print('Freq: ', freq)
                    try:
                        phase_orientation = locate_degree(timestamp, phase_after, f'{tag1}_{tag2}', freq)
                        pre_phase_orientation = phase_orientation
                    except Exception:
                        phase_orientation = pre_phase_orientation

                    phase_mat[:, col] = np.array(phase_orientation)
                    col += 1

                save_path = f'{rotation_level}/{tag1}_{tag2}/{tag1}_{tag2}{rotation_level_abbr}' \
                            f'({count_i})({count_j})_swap_f{swap_freq_count}.csv '
                np.savetxt(save_path, phase_mat, delimiter=',')

        swap_freq_count += 1

else:
    for count in range(26, 28):
        # 最终得到的相位矩阵，9个角度（9行），8个频率（8列）
        phase_mat = np.zeros((9, 8))

        col = 0
        # 上一轮循环中的phase_orientation
        pre_phase_orientation = []
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
            print('Freq: ', freq)
            try:
                phase_orientation = locate_degree(timestamp, phase_after, f'{tag1}_{tag2}', freq)
                pre_phase_orientation = phase_orientation
            except Exception:
                phase_orientation = pre_phase_orientation

            phase_mat[:, col] = np.array(phase_orientation)
            col += 1

        save_path = f'{rotation_level}/{tag1}_{tag2}/{tag1}_{tag2}{rotation_level_abbr}({count}).csv'
        np.savetxt(save_path, phase_mat, delimiter=',')
