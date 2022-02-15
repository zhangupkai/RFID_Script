import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks


# data = np.array(pd.read_csv('../phase_time_sequence/B016_AA03.csv', header=None))
# timestamp = data[:, 0]
# phase = data[:, 1]

def locate_degree_B016_AA03(phase):
    # 定位 B034_AA03 时间序列中的峰值，对应 degree_0, degree_360
    peaks, _ = find_peaks(phase, height=1.3, distance=2000)
    print('peaks: ', peaks)
    # # 两个峰值之间的间隔inter 对应 360度，则 inter/8 对应45度
    # peek_interval = []
    # for index in range(peaks.size):
    #     if index > 0:
    #         peek_interval.append(peaks[index] - peaks[index - 1])
    #     print(phase[peaks[index]])

    degree_0 = phase[peaks[0]]
    degree_360 = phase[peaks[1]]

    valleys, _ = find_peaks(-phase, height=-0.6, distance=2000)
    print('valleys: ', valleys)
    # 第一个峰之后的低谷为有效低谷，对应degree_180
    to_del_valleys_idx = []
    for index in range(valleys.shape[0]):
        # 删除在第一个较高峰之前的低谷
        if valleys[index] < peaks[0]:
            to_del_valleys_idx.append(index)

    valleys = np.delete(valleys, to_del_valleys_idx)

    degree_180 = phase[valleys[0]]

    degree_45 = phase[peaks[0] + (valleys[0] - peaks[0]) // 4]
    degree_90 = phase[peaks[0] + (valleys[0] - peaks[0]) // 2]
    degree_135 = phase[valleys[0] - (valleys[0] - peaks[0]) // 4]
    degree_225 = phase[valleys[0] + (peaks[1] - valleys[0]) // 4]
    degree_270 = phase[valleys[0] + (peaks[1] - valleys[0]) // 2]
    degree_315 = phase[peaks[1] - (peaks[1] - valleys[0]) // 4]

    phase_orientation = [degree_0, degree_45, degree_90,
                         degree_135, degree_180, degree_225,
                         degree_270, degree_315, degree_360]

    return phase_orientation
