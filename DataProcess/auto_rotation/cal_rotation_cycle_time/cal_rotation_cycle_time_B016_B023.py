import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks


# 计算当前转速下 B016_B023 转一圈的 所需时长
def cal_rotation_cycle_time_B016_B023(timestamp, phase):
    # 定位 B016_B023 时间序列中的峰值，前三个峰（height > 0.4）对应 degree_0, degree_180, degree_360
    # height=0.4 => 峰值最小高度为0.4
    # distance=1000 => 相邻峰之间的样本距离至少为1000，首先删除较小的峰
    peaks, _ = find_peaks(phase, height=0.4, distance=1000)

    print('peaks: ', peaks)
    print('size of peaks', peaks.size)

    # 第一个高峰对应 degree_0, 第三个高峰degree_360
    # degree_0 = phase[peaks[0]]
    # degree_180 = phase[peaks[1]]
    # degree_360 = phase[peaks[2]]

    # 返回一个周期的时间戳长度，微秒级时间戳
    return timestamp[peaks[2]] - timestamp[peaks[0]]
