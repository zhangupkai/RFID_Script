import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

from scipy.interpolate import interpolate

from filters import hampel
from cal_rotation_cycle_time_main import cal_rotation_cycle_time
from scipy.signal import find_peaks
from utils.base_list import get_freq_list

"""
转动标签对，相位差随时间（角度）的变化
Group1.3  8个不同频率下的数据 
"""
# tag1 = 'B034'
# tag2 = 'B029'

# tag1 = 'B016'
# tag2 = 'B023'

# tag1 = 'B016'
# tag2 = 'AA03'

# tag1 = 'F001'
# tag2 = 'F005'

# tag1 = 'E002'
# tag2 = 'C001'

# tag1 = 'E002'
# tag2 = 'E006'

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
rotation_level = 'final_experiment/4_tag_distance/distance_2'
# rotation_level = 'final_experiment/6_interfer_tag_numbers/interfer_2'
# rotation_level = 'final_experiment/7_object_material/material_2'
is_inter_deal = True
# count = 22
for count in range(26, 28):
    for freq in get_freq_list():
        bath_dir = f'../../data/tagPair/{rotation_level}/{tag1}_{tag2}/{tag1}_{tag2}({count})_25.0_{freq}.csv'
        df = pd.read_csv(bath_dir, header=None, names=['epc', 'freq', 'timestamp', 'phase', 'rssi'])

        pre_epc = ''
        if is_inter_deal is True:
            for index, row in df.iterrows():
                if index == 0:
                    pre_epc = row['epc']
                    continue
                # 如果当前行的epc等于上一行的epc，删除上一行
                if row['epc'] == pre_epc:
                    df = df.drop(index - 1)
                pre_epc = row['epc']

        # 不根据频率分组
        # 根据epc对数据进行分组
        grouped = df.groupby('epc')
        tag_info1 = np.array(grouped.get_group(tag1))
        tag_info2 = np.array(grouped.get_group(tag2))

        tag_info1_size = tag_info1.shape[0]
        tag_info2_size = tag_info2.shape[0]

        if tag_info1_size > tag_info2_size:
            tag_info1 = tag_info1[:tag_info2_size, :]
        elif tag_info1_size < tag_info2_size:
            tag_info2 = tag_info2[:tag_info1_size, :]

        timestamp1 = tag_info1[:, 2]
        phase1 = tag_info1[:, 3]
        timestamp2 = tag_info2[:, 2]
        phase2 = tag_info2[:, 3]

        # 计算差值并去除异常值
        phase_diff = hampel(np.abs(phase1 - phase2))
        # phase_diff = np.abs(phase1 - phase2)
        # 差值大于PI，减2PI操作
        for index in range(len(phase_diff)):
            if phase_diff[index] > math.pi:
                phase_diff[index] -= 2 * math.pi
        phase_diff = hampel(np.abs(phase_diff))

        # 插值后x轴
        timestamp_new = np.linspace(timestamp1[0], timestamp1[timestamp1.shape[0] - 1], timestamp1.shape[0] * 8)

        # print('k:', list(phase_timestamp.keys()), ' v:', list(phase_timestamp.values()))
        # 数据插值
        f = interpolate.interp1d(list(timestamp1), list(phase_diff), kind='slinear', fill_value="extrapolate")
        phase_new = f(timestamp_new)

        # 组合时间戳和相位差值
        phase_time = np.vstack((timestamp_new, phase_new)).T
        np.savetxt(f'phase_time_sequence/{rotation_level}/{tag1}_{tag2}({count})_{freq}.csv', phase_time, delimiter=',')

        plt.title(f'Phase Orientation Time (Tag Pair freq_{freq} {tag1}_{tag2}_c{count})')
        plt.scatter(x=timestamp_new, y=phase_new, alpha=0.4, s=0.6)
        plt.show()
