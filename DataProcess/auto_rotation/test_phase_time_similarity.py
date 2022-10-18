from time_series_similarity import *
import pandas as pd
import numpy as np

"""
计算天线-标签不同偏移角度下的相位-时间序列的相似度
"""


# 时间序列裁剪，每间隔一段距离取一个值
# s: 原始序列, step: 间隔取值的步长
def time_sequence_clip(s, step=100):
    s_clip = []
    idx = 0
    s_size = s.shape[0]
    while idx < s_size:
        s_clip.append(s[idx])
        idx += step
    return np.array(s_clip)


def cal_sequence_similarity(df_phase_time_1, df_phase_time_2):
    phase_time_1 = np.array(df_phase_time_1)
    phase_time_2 = np.array(df_phase_time_2)
    # phase_time_3 = np.array(df_phase_time_3)

    phase_1 = time_sequence_clip(phase_time_1[:, 1])
    phase_2 = time_sequence_clip(phase_time_2[:, 1])
    # phase_3 = time_sequence_clip(phase_time_3[:, 1])

    # 原始算法
    distance12, paths12, max_sub12 = TimeSeriesSimilarityImprove(phase_1, phase_2)
    # distance13, paths13, max_sub13 = TimeSeriesSimilarityImprove(phase_1, phase_3)
    # print("更新前 phase_1 和 phase_2 距离：" + str(distance12))
    # print("更新前 phase_1 和 phase_3 距离：" + str(distance13))

    # 衰减系数
    weight12 = calculate_attenuate_weight(len(phase_1), len(phase_2), max_sub12)
    # weight13 = calculate_attenuate_weight(len(phase_1), len(phase_3), max_sub13)

    # 更新距离
    distance12_improve = distance12 * weight12
    # distance13_improve = distance13 * weight13
    # print("更新后 phase_1 和 phase_2 距离：" + str(distance12_improve))
    # print("更新后 phase_1 和 phase_3 距离：" + str(distance13_improve))
    print("phase_1 和 phase_2 距离：" + str(distance12_improve))


if __name__ == '__main__':
    df_phase_time_1 = pd.read_csv('phase_time_sequence/extra_experiment/test_facing/2_right_45/D162_D163(2).csv')
    df_phase_time_2 = pd.read_csv('phase_time_sequence/extra_experiment/test_facing/0_facing/D162_D163(3).csv')
    # df_phase_time_3 = pd.read_csv('phase_time_sequence/extra_experiment/test_facing/1_left_45/D162_D163(1).csv')
    cal_sequence_similarity(df_phase_time_1, df_phase_time_2)
