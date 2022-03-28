import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# data = np.array(pd.read_csv('../phase_time_sequence/B034_B029.csv', header=None))
# timestamp = data[:, 0]
# phase = data[:, 1]


def locate_degree_B016_B023(phase):
    # 定位 B016_B023 时间序列中的峰值，前三个峰（height > 0.4）对应 degree_0, degree_180, degree_360
    # height=0.4 => 峰值最小高度为0.4
    # distance=1000 => 相邻峰之间的样本距离至少为1000，首先删除较小的峰
    peaks, _ = find_peaks(phase, height=0.4, distance=1000)

    # 找到第一个较高峰（height > 0.5）
    # 较高峰和较低峰是交替出现的，如果第一个是较低峰，则第二个一定是较高峰 ==> 移除第一个较低峰的数据
    # if phase[peaks[0]] < 0.5:
    #     peaks = np.delete(peaks, [0])

    print('peaks: ', peaks)

    # 第一个较高峰对应 degree_0
    degree_0 = phase[peaks[0]]
    degree_180 = phase[peaks[1]]
    degree_360 = phase[peaks[2]]

    # 定位 B016_B023 时间序列中的谷值，对应degree_90, degree_270
    valleys, _ = find_peaks(-phase, height=-0.1, distance=1000)

    # 第一个峰之后的低谷为有效低谷，对应degree_90
    to_del_valleys_idx = []
    for index in range(valleys.shape[0]):
        # 删除在第一个峰之前的低谷
        if valleys[index] < peaks[0]:
            to_del_valleys_idx.append(index)

    valleys = np.delete(valleys, to_del_valleys_idx)

    print('valleys: ', valleys)

    degree_90 = phase[valleys[0]]
    degree_270 = phase[valleys[1]]

    degree_45 = phase[peaks[0] + (valleys[0] - peaks[0]) // 2]
    degree_135 = phase[valleys[0] + (peaks[1] - valleys[0]) // 2]

    degree_225 = phase[peaks[1] + (valleys[1] - peaks[1]) // 2]
    degree_315 = phase[valleys[1] + (peaks[2] - valleys[1]) // 2]

    phase_orientation = [degree_0, degree_45, degree_90,
                         degree_135, degree_180, degree_225,
                         degree_270, degree_315, degree_360]

    return phase_orientation
