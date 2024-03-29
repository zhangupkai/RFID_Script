import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks


# character01
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


# character02
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


# character03
def locate_degree_B034_B029(phase):
    # 定位 B034_B029 时间序列中的峰值，前两个较高峰（height > 0.5）对应 degree_0, degree_360
    #                               两个较高峰之间的一个较低峰（height < 0.5）对应 degree_180
    # height=0.3 => 峰值最小高度为0.3
    # distance=1000 => 相邻峰之间的样本距离至少为1000，首先删除较小的峰
    peaks, _ = find_peaks(phase, height=0.3, distance=1000)

    # 找到第一个较高峰（height > 0.5）
    # 较高峰和较低峰是交替出现的，如果第一个是较低峰，则第二个一定是较高峰 ==> 移除第一个较低峰的数据
    if phase[peaks[0]] < 0.5:
        peaks = np.delete(peaks, [0])

    print('peaks: ', peaks)

    # 第一个较高峰对应 degree_0
    degree_0 = phase[peaks[0]]
    degree_180 = phase[peaks[1]]
    degree_360 = phase[peaks[2]]

    # 定位 B034_B029 时间序列中的谷值，对应degree_90, degree_270
    valleys, _ = find_peaks(-phase, height=-0.2, distance=1000)

    # 第一个较高峰之后的低谷为有效低谷，对应degree_90
    to_del_valleys_idx = []
    for index in range(valleys.shape[0]):
        # 删除在第一个较高峰之前的低谷
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


# character04
def locate_degree_E002_C001(phase, freq):
    # 定位 E002_C001 时间序列中的峰值，最高等对应 degree_135
    # height=1.0 => 峰值最小高度为1.0
    # distance=1000 => 相邻峰之间的样本距离至少为1000，首先删除较小的峰
    peaks, _ = find_peaks(phase, height=1.3, distance=1000)

    print('peaks: ', peaks)

    # 周期除以8
    peak_interval_unit = (peaks[1] - peaks[0]) // 8
    degree_135 = phase[peaks[0]]
    degree_90 = phase[peaks[0] - peak_interval_unit]
    degree_45 = phase[peaks[0] - peak_interval_unit * 2]
    degree_0 = phase[peaks[0] - peak_interval_unit * 3]
    degree_180 = phase[peaks[0] + peak_interval_unit]
    degree_225 = phase[peaks[0] + peak_interval_unit * 2]
    degree_270 = phase[peaks[0] + peak_interval_unit * 3]
    degree_315 = phase[peaks[0] + peak_interval_unit * 4]
    degree_360 = phase[peaks[0] + peak_interval_unit * 5]

    phase_orientation = [degree_0, degree_45, degree_90,
                         degree_135, degree_180, degree_225,
                         degree_270, degree_315, degree_360]

    return phase_orientation


# character05
def locate_degree_E002_E006(phase, freq):
    # 定位 E002_E006 时间序列中的峰值，第一个较低峰对应degree_135，第一个较高峰对应degree_315
    # level 2 ==> distance=6000
    peaks, _ = find_peaks(phase, height=0.5, distance=6000)

    # 找到第一个较低峰
    # 较高峰和较低峰是交替出现的，如果第一个是较高峰，则第二个一定是较低峰 ==> 移除第一个较高峰的数据
    if phase[peaks[0]] > phase[peaks[1]]:
        peaks = np.delete(peaks, [0])

    print('peaks: ', peaks)

    # 第一个较低峰对应 degree_135
    degree_135 = phase[peaks[0]]
    degree_315 = phase[peaks[1]]

    # 定位 E002_E006 时间序列中的谷值，对应degree_90, degree_270
    # level 2 ==> distance=6000
    valleys, _ = find_peaks(-phase, height=-0.2, distance=6000)

    print('valleys: ', valleys)

    # 第一个较低峰之后的低谷为有效低谷，对应degree_270
    to_del_valleys_idx = []
    for index in range(valleys.shape[0]):
        # 删除在第一个较高峰之前的低谷
        if valleys[index] < peaks[0]:
            to_del_valleys_idx.append(index)

    valleys = np.delete(valleys, to_del_valleys_idx)

    # 第一个较低峰之后的低谷为第一个有效低谷，对应degree_270
    # 第二个有效低谷，对应degree_90
    degree_270 = phase[valleys[0]]
    degree_90 = phase[valleys[1]]

    degree_180 = phase[peaks[0] + (valleys[0] - peaks[0]) // 3]
    degree_225 = phase[valleys[0] - (valleys[0] - peaks[0]) // 3]
    degree_360 = phase[peaks[1] + (valleys[1] - peaks[1]) // 3]
    degree_0 = phase[peaks[1] + (valleys[1] - peaks[1]) // 3]
    degree_45 = phase[valleys[1] - (valleys[1] - peaks[1]) // 3]

    phase_orientation = [degree_0, degree_45, degree_90,
                         degree_135, degree_180, degree_225,
                         degree_270, degree_315, degree_360]

    return phase_orientation


# character06
def locate_degree_F001_F005(phase, freq):
    # 定位 F001_F005 时间序列中的峰值，
    # 低峰，高峰，低峰，高峰，分别对应 degree_45, degree_135, degree_225, degree_315
    # level 4 ==> distance=2500
    # level 2 ==>
    peaks, _ = find_peaks(phase, height=0.15, distance=5000)

    # 删除离起始点过近的数据
    if peaks[0] < 30:
        peaks = np.delete(peaks, [0])

    # 找到第一个较低峰
    # 较高峰和较低峰是交替出现的，如果第一个是较高峰，则第二个一定是较低峰 ==> 移除第一个较高峰的数据
    if phase[peaks[0]] > phase[peaks[1]] or phase[peaks[0]] > 0.4:
        peaks = np.delete(peaks, [0])

    print('peaks: ', peaks)

    # 第一个低峰对应 degree_45
    degree_45 = phase[peaks[0]]
    degree_135 = phase[peaks[1]]
    degree_225 = phase[peaks[2]]
    degree_315 = phase[peaks[3]]

    # 定位 F001_F005 时间序列中的谷值，对应degree_90, degree_270
    # level 4 ==> distance=6000
    valleys, _ = find_peaks(-phase, height=-0.05, distance=12000)

    # 第一个峰之后的谷为有效谷，对应degree_90
    to_del_valleys_idx = []
    for index in range(valleys.shape[0]):
        # 删除在第一个较高峰之前的低谷
        if valleys[index] < peaks[0]:
            to_del_valleys_idx.append(index)

    valleys = np.delete(valleys, to_del_valleys_idx)

    print('valleys: ', valleys)

    degree_90 = phase[valleys[0]]
    degree_270 = phase[valleys[1]]

    degree_180 = phase[peaks[1] + (valleys[1] - peaks[1]) // 3]
    degree_360 = phase[peaks[3] + (valleys[2] - peaks[3]) // 3]
    degree_0 = phase[peaks[3] + (valleys[2] - peaks[3]) // 3]

    phase_orientation = [degree_0, degree_45, degree_90,
                         degree_135, degree_180, degree_225,
                         degree_270, degree_315, degree_360]

    return phase_orientation


# character07
def locate_degree_F001_E006(phase, freq):
    # 定位 F001_E006 时间序列中的谷值，对应degree_225
    valleys, _ = find_peaks(-phase, height=-1.5, distance=2000)
    print('valleys: ', valleys)

    degree_225 = phase[valleys[0]]

    # 定位 F001_E006 时间序列中的峰值，最高等对应 degree_315
    peaks, _ = find_peaks(phase, height=2.6, distance=1000)
    print('peaks: ', peaks)

    # 第一个谷之后的低谷为有效峰，对应degree_315
    to_del_peaks_idx = []
    for index in range(peaks.shape[0]):
        # 删除在第一个谷之前的峰
        if peaks[index] < valleys[0]:
            to_del_peaks_idx.append(index)

    peaks = np.delete(peaks, to_del_peaks_idx)

    degree_315 = phase[peaks[0]]

    degree_270 = phase[valleys[0] + (peaks[0] - valleys[0]) // 2]
    degree_360 = phase[peaks[0] + (valleys[1] - peaks[0]) // 6]
    degree_0 = phase[peaks[0] + (valleys[1] - peaks[0]) // 6]
    degree_45 = phase[peaks[0] + (valleys[1] - peaks[0]) // 3]
    degree_90 = phase[peaks[0] + (valleys[1] - peaks[0]) // 2]
    degree_135 = phase[peaks[1] - (valleys[1] - peaks[0]) // 3]
    degree_180 = phase[peaks[1] - (valleys[1] - peaks[0]) // 6]

    phase_orientation = [degree_0, degree_45, degree_90,
                         degree_135, degree_180, degree_225,
                         degree_270, degree_315, degree_360]

    return phase_orientation


# character08
def locate_degree_C001_C002(phase, freq):
    return locate_degree_C003_C004(phase, freq)


# character09
def locate_degree_C003_C004(phase, freq):
    # 定位 C003_C004 时间序列中的峰，一个周期有一个最高峰
    # 对应 degree_135
    #
    # level 2 ==> distance=30000
    # level 3 ==> distance=18000
    # level 4 ==> distance=13000
    peaks, _ = find_peaks(phase, height=0.45, distance=13000)

    # if peaks[0] < 200:
    #     peaks = np.delete(peaks, [0])

    print('Before del, peaks: ', peaks)

    # 定位 C003_C004 时间序列中的谷值，对应degree_90, degree_270
    # level 2 ==> distance=15000
    # level 3 ==> distance=8000
    # level 4 ==> distance=5000
    valleys, _ = find_peaks(-phase, height=-0.1, distance=5000)

    print('Before del, valleys: ', valleys)

    # 第一个高峰之后的低谷为有效低谷，对应degree_270
    to_del_valleys_idx = []
    for index in range(valleys.shape[0]):
        # 删除在第一个较高峰之前的低谷
        if valleys[index] < peaks[0]:
            to_del_valleys_idx.append(index)

    valleys = np.delete(valleys, to_del_valleys_idx)

    print('After  del, peaks: ', peaks)

    print('After  del, valleys: ', valleys)

    degree_135 = phase[peaks[0]]
    degree_270 = phase[valleys[0]]
    degree_90 = phase[valleys[1]]

    degree_180 = phase[peaks[0] + (valleys[0] - peaks[0]) // 3]
    degree_225 = phase[valleys[0] - (valleys[0] - peaks[0]) // 3]

    degree_315 = phase[valleys[0] + (valleys[1] - valleys[0]) // 4]
    degree_360 = phase[valleys[0] + (valleys[1] - valleys[0]) // 2]
    degree_0 = phase[valleys[0] + (valleys[1] - valleys[0]) // 2]
    degree_45 = phase[valleys[1] - (valleys[1] - valleys[0]) // 4]

    phase_orientation = [degree_0, degree_45, degree_90,
                         degree_135, degree_180, degree_225,
                         degree_270, degree_315, degree_360]

    return phase_orientation


# character10
def locate_degree_E004_E005(phase, freq):
    # 定位 E004_E005 时间序列中的峰，一个周期有一个最高峰
    # 峰仅用于第一个有效谷，不用于定位具体角度
    #
    # level 2 ==> distance=15000
    # level 3 ==> distance=18000
    # level 4 ==> distance=10000
    peaks, _ = find_peaks(phase, height=0.45, distance=10000)

    # if peaks[0] < 200:
    #     peaks = np.delete(peaks, [0])

    print('Before del, peaks: ', peaks)

    # 定位 E004_E005 时间序列中的谷值，对应degree_90, degree_270
    # level 2 ==> distance=7000
    # level 3 ==> distance=7000
    # level 4 ==> distance=5000
    valleys, _ = find_peaks(-phase, height=-0.1, distance=5000)

    print('Before del, valleys: ', valleys)

    # 第一个高峰之后的低谷为有效低谷，对应degree_90
    to_del_valleys_idx = []
    for index in range(valleys.shape[0]):
        # 删除在第一个较高峰之前的低谷
        if valleys[index] < peaks[0]:
            to_del_valleys_idx.append(index)

    valleys = np.delete(valleys, to_del_valleys_idx)

    print('After  del, peaks: ', peaks)

    print('After  del, valleys: ', valleys)

    if valleys.size >= 3:
        degree_90 = phase[valleys[0]]
        degree_270 = phase[valleys[1]]

        degree_135 = phase[valleys[0] + (valleys[1] - valleys[0]) // 4]
        degree_180 = phase[valleys[0] + (valleys[1] - valleys[0]) // 2]
        degree_225 = phase[valleys[1] - (valleys[1] - valleys[0]) // 4]

        degree_315 = phase[valleys[1] + (valleys[2] - valleys[1]) // 4]
        degree_360 = phase[valleys[1] + (valleys[2] - valleys[1]) // 2]
        degree_0 = phase[valleys[1] + (valleys[2] - valleys[1]) // 2]
        degree_45 = phase[valleys[2] - (valleys[2] - valleys[1]) // 4]

        phase_orientation = [degree_0, degree_45, degree_90,
                             degree_135, degree_180, degree_225,
                             degree_270, degree_315, degree_360]

        return phase_orientation

    else:

        degree_90 = phase[valleys[0]]
        degree_270 = phase[valleys[1]]

        degree_0 = phase[valleys[0] - (valleys[1] - valleys[0]) // 2]
        degree_45 = phase[valleys[0] - (valleys[1] - valleys[0]) // 4]

        degree_135 = phase[valleys[0] + (valleys[1] - valleys[0]) // 4]
        degree_180 = phase[valleys[0] + (valleys[1] - valleys[0]) // 2]
        degree_225 = phase[valleys[1] - (valleys[1] - valleys[0]) // 4]

        degree_315 = phase[valleys[1] + (valleys[1] - valleys[0]) // 4]
        degree_360 = phase[valleys[1] + (valleys[1] - valleys[0]) // 2]

        phase_orientation = [degree_0, degree_45, degree_90,
                             degree_135, degree_180, degree_225,
                             degree_270, degree_315, degree_360]

        return phase_orientation


# character11
def locate_degree_F002_F003(phase, freq):
    # 定位 F002_F003 时间序列中的峰，一个周期有一个最高峰
    # 峰仅用于第一个有效谷，不用于定位具体角度
    #
    # level 2 ==> distance=15000
    # level 3 ==> distance=10000
    # level 4 ==> distance=10000
    peaks, _ = find_peaks(phase, height=0.7, distance=10000)

    # if peaks[0] < 200:
    #     peaks = np.delete(peaks, [0])

    print('Before del, peaks: ', peaks)

    # 定位 F002_F003 时间序列中的谷值，对应degree_90, degree_270
    # level 2 ==> distance=7000
    # level 3 ==> distance=7000
    # level 4 ==> distance=5000
    valleys, _ = find_peaks(-phase, height=-0.1, distance=5000)

    print('Before del, valleys: ', valleys)

    # 第一个高峰之后的低谷为有效低谷，对应degree_90
    to_del_valleys_idx = []
    for index in range(valleys.shape[0]):
        # 删除在第一个较高峰之前的低谷
        if valleys[index] < peaks[0]:
            to_del_valleys_idx.append(index)

    valleys = np.delete(valleys, to_del_valleys_idx)

    print('After  del, peaks: ', peaks)

    print('After  del, valleys: ', valleys)

    if valleys.size >= 3:
        degree_90 = phase[valleys[0]]
        degree_270 = phase[valleys[1]]

        degree_135 = phase[valleys[0] + (valleys[1] - valleys[0]) // 4]
        degree_180 = phase[valleys[0] + (valleys[1] - valleys[0]) // 2]
        degree_225 = phase[valleys[1] - (valleys[1] - valleys[0]) // 4]

        degree_315 = phase[valleys[1] + (valleys[2] - valleys[1]) // 4]
        degree_360 = phase[valleys[1] + (valleys[2] - valleys[1]) // 2]
        degree_0 = phase[valleys[1] + (valleys[2] - valleys[1]) // 2]
        degree_45 = phase[valleys[2] - (valleys[2] - valleys[1]) // 4]

        phase_orientation = [degree_0, degree_45, degree_90,
                             degree_135, degree_180, degree_225,
                             degree_270, degree_315, degree_360]

        return phase_orientation

    else:

        degree_90 = phase[valleys[0]]
        degree_270 = phase[valleys[1]]

        degree_0 = phase[valleys[0] - (valleys[1] - valleys[0]) // 2]
        degree_45 = phase[valleys[0] - (valleys[1] - valleys[0]) // 4]

        degree_135 = phase[valleys[0] + (valleys[1] - valleys[0]) // 4]
        degree_180 = phase[valleys[0] + (valleys[1] - valleys[0]) // 2]
        degree_225 = phase[valleys[1] - (valleys[1] - valleys[0]) // 4]

        degree_315 = phase[valleys[1] + (valleys[1] - valleys[0]) // 4]
        degree_360 = phase[valleys[1] + (valleys[1] - valleys[0]) // 2]

        phase_orientation = [degree_0, degree_45, degree_90,
                             degree_135, degree_180, degree_225,
                             degree_270, degree_315, degree_360]

        return phase_orientation


# character common
def locate_degree_common(phase, freq):
    # 定位 时间序列中的峰，一个周期有一个最高峰
    # 峰仅用于第一个有效谷，不用于定位具体角度
    # level 4 ==> distance=10000
    peaks, _ = find_peaks(phase, height=0.15, distance=10000)

    # if peaks[0] < 200:
    #     peaks = np.delete(peaks, [0])

    print('Before del, peaks: ', peaks)

    # 定位 时间序列中的谷值，对应degree_90, degree_270
    # level 4 ==> distance=5000
    valleys, _ = find_peaks(-phase, height=-0.15, distance=5000)

    print('Before del, valleys: ', valleys)

    # 第一个高峰之后的低谷为有效低谷，对应degree_90
    to_del_valleys_idx = []
    for index in range(valleys.shape[0]):
        # 删除在第一个较高峰之前的低谷
        if valleys[index] < peaks[0]:
            to_del_valleys_idx.append(index)

    valleys = np.delete(valleys, to_del_valleys_idx)

    print('After  del, peaks: ', peaks)

    print('After  del, valleys: ', valleys)

    if valleys.size >= 3:
        degree_90 = phase[valleys[0]]
        degree_270 = phase[valleys[1]]

        degree_135 = phase[valleys[0] + (valleys[1] - valleys[0]) // 4]
        degree_180 = phase[valleys[0] + (valleys[1] - valleys[0]) // 2]
        degree_225 = phase[valleys[1] - (valleys[1] - valleys[0]) // 4]

        degree_315 = phase[valleys[1] + (valleys[2] - valleys[1]) // 4]
        degree_360 = phase[valleys[1] + (valleys[2] - valleys[1]) // 2]
        degree_0 = phase[valleys[1] + (valleys[2] - valleys[1]) // 2]
        degree_45 = phase[valleys[2] - (valleys[2] - valleys[1]) // 4]

        phase_orientation = [degree_0, degree_45, degree_90,
                             degree_135, degree_180, degree_225,
                             degree_270, degree_315, degree_360]

        return phase_orientation

    else:

        degree_90 = phase[valleys[0]]
        degree_270 = phase[valleys[1]]

        degree_0 = phase[valleys[0] - (valleys[1] - valleys[0]) // 2]
        degree_45 = phase[valleys[0] - (valleys[1] - valleys[0]) // 4]

        degree_135 = phase[valleys[0] + (valleys[1] - valleys[0]) // 4]
        degree_180 = phase[valleys[0] + (valleys[1] - valleys[0]) // 2]
        degree_225 = phase[valleys[1] - (valleys[1] - valleys[0]) // 4]

        degree_315 = phase[valleys[1] + (valleys[1] - valleys[0]) // 4]
        degree_360 = phase[valleys[1] + (valleys[1] - valleys[0]) // 2]

        phase_orientation = [degree_0, degree_45, degree_90,
                             degree_135, degree_180, degree_225,
                             degree_270, degree_315, degree_360]

        return phase_orientation

