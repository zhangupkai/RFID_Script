import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.signal import find_peaks


# 转动标签对，相位差随时间（角度）的变化
# tag1 = 'B034'
# tag2 = 'B029'

tag1 = 'B016'
tag2 = 'B023'

# tag1 = 'B016'
# tag2 = 'AA03'

is_grouped = True
count = 12
bath_dir = f'../../data/tagPair/auto_rotation/{tag1}_{tag2}/{tag1}_{tag2}({count})_25.0.csv'
df = pd.read_csv(bath_dir, header=None, names=['epc', 'freq', 'timestamp', 'phase', 'rssi'])

if is_grouped is True:
    # TODO 根据频率freq对原始数据进行分组，再进行后续处理
    group_by_freq = df.groupby('freq')

    for freq, freq_group in group_by_freq:
        # df中的数据应该是两个标签交替出现的，若出现连续的标签，需要记录非第一次出现的行号index而后删除
        # 记录应该删除的数据行号index
        # to_del_index = []
        # for index, row in df.iterrows():
        #     if index == 0:
        #         # 记录上一行数据
        #         pre_row = row
        #     else:
        #         if row['epc'] == pre_row['epc']:
        #             to_del_index.append(index)
        #         pre_row = row

        # 删除指定数据
        # df.drop(to_del_index, inplace=True)

        # 根据epc对数据进行分组
        grouped = freq_group.groupby('epc')
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
        phase_diff = np.abs(phase1 - phase2)
        # 差值大于PI，减2PI操作
        for index in range(len(phase_diff)):
            if phase_diff[index] > math.pi:
                phase_diff[index] -= 2 * math.pi
        phase_diff = np.abs(phase_diff)

        # plt.scatter(x=x_phase1, y=phase1, c='red', alpha=0.4, s=0.6)
        # plt.scatter(x=x_phase2, y=phase2, alpha=0.4, s=0.6)
        plt.title(f'Phase Orientation Time (Tag Pair freq_{freq} {tag1}_{tag2}_c{count})')
        plt.scatter(x=timestamp1, y=phase_diff, alpha=0.4, s=0.6)
        plt.show()

        # 组合时间戳和相位差值
        phase_time = np.vstack((timestamp1, phase_diff)).T
        np.savetxt(f'phase_time_sequence/{tag1}_{tag2}({count})_{freq}.csv', phase_time, delimiter=',')

        # plt.scatter(x=timestamp1, y=phase1, alpha=0.4, s=0.6, label=tag1)
        # plt.scatter(x=timestamp2, y=phase2, alpha=0.4, s=0.6, label=tag2, c='red')
        # plt.legend()
        # plt.show()

else:
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
    phase_diff = np.abs(phase1 - phase2)
    # 差值大于PI，减2PI操作
    for index in range(len(phase_diff)):
        if phase_diff[index] > math.pi:
            phase_diff[index] -= 2 * math.pi
    phase_diff = np.abs(phase_diff)

    plt.title(f'Phase Orientation Time (Tag Pair freq_all {tag1}_{tag2}_c{count})')
    plt.scatter(x=timestamp1, y=phase_diff, alpha=0.4, s=0.6)
    plt.show()
