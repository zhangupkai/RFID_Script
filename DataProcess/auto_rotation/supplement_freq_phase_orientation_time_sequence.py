import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import interpolate
from filters import hampel
from base_list import get_freq_list
from locate_degree_main import locate_degree

# 补全单个频率下的 相位-角度-时间序列
# TODO 去除离群值 插值

# tag1 = 'B034'
# tag2 = 'B029'
tag1 = 'B016'
tag2 = 'AA03'
count = 23
# freq = 920.625

# 最终得到的相位矩阵，9个角度（9行），8个频率（8列）
phase_mat = np.zeros((9, 8))

col = 0
for freq in get_freq_list():
    bath_dir = f'phase_time_sequence/{tag1}_{tag2}({count})_{freq}.csv'
    data = np.array(pd.read_csv(bath_dir, header=None))
    timestamp = data[:, 0]
    phase = data[:, 1]
    size = timestamp.shape[0]

    # plt.title('Phase Orientation Time (Before Denoising)')
    # plt.scatter(timestamp, phase, alpha=0.4, s=0.6)
    # plt.show()

    # 去除异常值
    phase_after = hampel(phase)

    # plt.title('Phase Orientation Time (After Denoising)')
    # plt.scatter(timestamp, phase_after, alpha=0.4, s=0.6)
    # plt.show()

    # 时间戳间隔
    timestamp_interval = []
    for index in range(timestamp.shape[0]):
        if index > 0:
            timestamp_interval.append(timestamp[index] - timestamp[index - 1])

    timestamp_interval = np.array(timestamp_interval)
    # plt.title("Timestamp Interval")
    # plt.scatter(x=np.arange(0, timestamp_interval.shape[0], 1), y=timestamp_interval, alpha=0.4, s=0.6)
    # plt.show()

    # 时间戳间隔的阈值，大于阈值说明时间戳发生跳变
    TIME_INTER_THRESHOLD = 10000000
    # timestamp_interval数组中大于阈值的索引
    exceed_time_inter_idx = np.where(timestamp_interval > TIME_INTER_THRESHOLD)[0]

    # 根据时间戳的跳变，对时间戳和相位数据进行分段（一个段为图中的一个竖条数据）
    split_timestamp = np.split(timestamp, exceed_time_inter_idx + 1)
    split_phase = np.split(phase_after, exceed_time_inter_idx + 1)
    # 每一段数据取其中位数作为特征点
    split_timestamp_median = []
    split_phase_median = []
    for index in range(len(split_phase)):
        split_phase_median.append(np.median(split_phase[index]))
        split_timestamp_median.append(np.median(split_timestamp[index]))

    # plt.title('Phase Orientation Time (Extract Feature Point)')
    # plt.scatter(x=split_timestamp_median, y=split_phase_median, alpha=0.8, s=10)
    # plt.show()

    # 插值后x轴，时间戳轴长度*8 Because: 一共8个频率数据
    timestamp_new = np.linspace(timestamp[0], timestamp[timestamp.shape[0] - 1], timestamp.shape[0] * 8)

    # 数据插值
    f = interpolate.interp1d(split_timestamp_median, split_phase_median, kind='cubic', fill_value="extrapolate")
    phase_new = f(timestamp_new)
    plt.title('Phase Orientation Time (Direct Interpolation)')
    plt.scatter(x=split_timestamp_median, y=split_phase_median, alpha=0.8, s=10)
    plt.plot(timestamp_new, phase_new)
    plt.show()

    # 单个频率下，在相位角度时间序列中定位到指定的9个角度
    phase_orientation = locate_degree(phase_new, f'{tag1}_{tag2}')
    phase_mat[:, col] = np.array(phase_orientation)
    col += 1

save_path = f'phase_mat_data/{tag1}_{tag2}/{tag1}_{tag2}({count}).csv'
np.savetxt(save_path, phase_mat, delimiter=',')
