from time_series_similarity import *
import pandas as pd
import numpy as np
import os
import csv

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
    return distance12_improve


def cal_two_sequence(path1, path2):
    # df_phase_time_1 = pd.read_csv('phase_time_sequence/extra_experiment/test_facing/5_left_14/D162_D163(2).csv')
    # df_phase_time_2 = pd.read_csv('phase_time_sequence/extra_experiment/test_facing/5_left_14/D162_D163(1).csv')
    df_phase_time_1 = pd.read_csv(path1)
    df_phase_time_2 = pd.read_csv(path2)
    return cal_sequence_similarity(df_phase_time_1, df_phase_time_2)


THRESHOLD = 0.35
if __name__ == '__main__':
    if True:
        bath_path = 'phase_time_sequence\\extra_experiment\\'
        path1 = f'{bath_path}rotation_offset_0\\D162_D163(1).csv'
        path2 = f'{bath_path}rotation_offset_left_5\\D162_D163(1).csv'
        similarity_distance = cal_two_sequence(path1, path2)
        print(similarity_distance)

    if False:
        bath_path = 'phase_time_sequence\\extra_experiment\\test_facing\\'
        filename_list = []
        for root, dir_names, filenames in os.walk(bath_path):
            for filename in filenames:
                filename_str = os.path.join(root, filename)
                filename_list.append(filename_str)
                # print(filename_list)

        final = []
        for path1 in filename_list:
            for path2 in filename_list:
                if path1 == path2:
                    continue
                # 两个path的路径前缀，即天线面对的方向
                path1_affix = path1[0:path1.rfind('\\')+1]
                path2_affix = path2[0:path2.rfind('\\')+1]
                # 实际上，两个path是否在同一方向
                actual_res = 0
                if path1_affix == path2_affix:
                    actual_res = 1

                # 计算两个path的相似距离
                similarity_distance = cal_two_sequence(path1, path2)

                # 实验中，对两个path是否在同一方向的判断结果
                experiment_res = 0
                if similarity_distance < THRESHOLD:
                    experiment_res = 1

                cur = [path1, path2, similarity_distance, actual_res, experiment_res]
                final.append(cur)

        f = open(f'{bath_path}\\result.csv', 'w', newline='')
        writer = csv.writer(f)
        for i in final:
            writer.writerow(i)
        f.close()

