import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import interpolate
from myunwrap import *
from pre_purpose import normalization
from my_dtw import *
from base_list import *


"""
同一距离下，不同标签的 相位-角度 曲线图
"""
if __name__ == '__main__':
    distance = '60cm'
    # tags = ['B023', 'B022', 'B016']
    tags = ['B023', 'B016']
    # colors = ['blue', 'red', 'black']
    colors = ['red', 'blue']

    bath_dir = 'phase_time_sequence/set_four_orientation/distance_' + distance + '/' + 'phase_freq_orientation/'

    # phase_mat = np.zeros((3, 9))

    degrees = ['degree_0', 'degree_45', 'degree_90', 'degree_135', 'degree_180',
               'degree_225', 'degree_270', 'degree_315', 'degree_360']

    similarity_list = []

    i = 0
    phase_mat = []
    matplotlib.rcParams.update({'font.size': 12})  # 改变所有字体大小，改变其他性质类似
    for tag in tags:

        file_path = bath_dir + tag + '.csv'

        data = np.array(pd.read_csv(file_path, header=None))
        # 取第一列数据（频率为920.875，整个csv文件中所有数据均为功率24dBm下测量）
        # phase_list = phase_time_sequence[:, 0]
        phase_list = data[0, :]

        # j = 0
        # for degree in degrees:
        #     file_path = bath_dir + tag + '_' + degree + '.csv'
        #     phase_time_sequence = np.array(pd.read_csv(file_path, header=None))
        #     # 取第一行第一列数据（功率为24dBm，频率为920.875）
        #     phase_list.append(phase_time_sequence[0, 0])
            # phase_mat[i, j] =phase_mean
            # j += 1

        # phase_mat[i, ] = phase_list
        # 归一化
        # phase_list = phase_list
        # x = [0, 45, 90, 135, 180, 225, 270, 315, 360]
        # x_new = np.arange(0, 360, 4.5)
        # func = interpolate.interp1d(x, phase_list, kind='cubic')
        # y_new = func(x_new)
        #
        # phase_mat.append(phase_list)
        # plt.plot(x_new, y_new, marker='o', markersize=3, color=colors[i], label=tag)
        plt.plot(get_freq_list(), phase_list, marker='o', markersize=3, color=colors[i], label=tag)

        i += 1

    plt.title("Distance " + distance)
    plt.xlabel("Freq")
    plt.ylabel("Degree")
    plt.legend()
    plt.show()

    # distance_similarity_origin = TimeSeriesSimilarity(phase_mat[0], phase_mat[1])
    distance_similarity = ImprovedTimeSeriesSimilarity(phase_mat[0], phase_mat[1])
    # np.savetxt(bath_dir + 'B016_B023_B023(2).csv', phase_mat, delimiter=',')
