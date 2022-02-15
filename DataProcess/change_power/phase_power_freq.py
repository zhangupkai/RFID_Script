import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys
import os
import math
import copy


def unwrap(raw_vector, cutoff=math.pi):
    if raw_vector is None or len(raw_vector) <= 0:
        print("warring: The vector is empty!")
        return None
    vector = list(copy.deepcopy(raw_vector))
    # 初始化变量
    m = len(vector)
    dp = []
    dp_corr = []
    roundDown = []
    cumsum = []
    # 计算递增的相位值
    for i in range(m - 1):
        dp.append(vector[i + 1] - vector[i])
    # 计算递增的相位值偏离多少个2PI
    for i in range(len(dp)):
        dp_corr.append(dp[i] / (2 * math.pi))
    # 对dp_corr进行舍入，以达到（2n+1）pi 被规整到2n*pi,而不是（2n+2）pi
    for i in range(len(dp_corr)):
        roundDown.append(abs(dp_corr[i] % 1) <= 0.5)
    # 按照以上注释中的思路整理数据
    for i in range(len(dp_corr)):
        if roundDown[i] == True:
            if dp_corr[i] > 0:
                dp_corr[i] = math.floor(dp_corr[i])
            else:
                dp_corr[i] = math.ceil(dp_corr[i])
        # 朝最近整数四舍五入
        else:
            dp_corr[i] = round(dp_corr[i])

    # 处理跳变，跳变大于cutoff才处理
    # cumsum 用来记录前i个跳变的累计影响，每前一个元素的加减，后续元素都要加减
    for i in range(len(dp)):
        if abs(dp[i]) < cutoff:
            dp_corr[i] = 0
        if i == 0:
            cumsum.append(dp_corr[i])
        else:
            cumsum.append(dp_corr[i] + cumsum[i - 1])

    # 规整
    for i in range(1, m):
        vector[i] = vector[i] - cumsum[i - 1] * 2 * math.pi

    # 对于数据点稀疏的情况，有些点的跳变没有超过2pi，需要进一步微调
    jumpoint = 3
    for i in range(m - 1):
        if vector[i + 1] - vector[i] > jumpoint:
            for j in range(i + 1, m):
                vector[j] = vector[j] - 2 * math.pi
            continue
        if vector[i] - vector[i + 1] > jumpoint:
            for j in range(i + 1, m):
                vector[j] = vector[j] + 2 * math.pi
    return vector


"""
处理原始数据，按距离、标签和角度存储数据
"""
if __name__ == '__main__':
    distance = 'distance_40cm'
    degrees = ['degree_0', 'degree_45', 'degree_90', 'degree_135', 'degree_180',
               'degree_225', 'degree_270', 'degree_315', 'degree_360']
    # degrees = ['degree_90']
    # group = 'group4'
    tag = 'B022'
    tag_in_path = 'B022'

    # 生成功率列表
    power_list = []
    for x in range(0, 8):
        power = 24.0 + x
        power_list.append(power)

    # 生成频率列表
    freq_list = []
    for x in range(0, 8):
        freq = 920.625 + x * 0.5
        freq_list.append(freq)

    for degree in degrees:
        bath_dir = '../../phase_time_sequence/changePower2/SetFourOrientation/' + distance + '/' + tag_in_path + '/' + degree + '/'
        phase_mat = np.zeros((8, 8))
        i = 0
        for power in power_list:
            j = 0
            for freq in freq_list:
                file_path = bath_dir + 'changePower2' + tag + '_' + str(power) + '_' + str(freq) + '.csv'
                print(file_path)
                # 文件不存在，进入下一轮循环
                if os.path.exists(file_path):
                    if os.stat(file_path).st_size > 0:
                        data = np.array(pd.read_csv(file_path, header=None))
                        # 相位均值
                        phase = np.mean(data[:, 3])
                        print(phase)
                        phase_mat[i, j] = phase
                j += 1
            # phase_mat[i, :] = unwrap(phase_mat[i, :])
            i += 1
        # unwrap_phase_list = unwrap(phase_mat.flatten())
        # unwrap_phase_mat = np.array(unwrap_phase_list).reshape(8, 8)

        np.savetxt('phase_time_sequence/set_four_orientation/' + distance + '/' + tag_in_path + '_' + degree + '.csv', phase_mat,
                   delimiter=',')
