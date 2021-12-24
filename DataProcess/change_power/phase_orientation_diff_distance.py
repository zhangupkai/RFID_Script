import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import interpolate
from myunwrap import *
from pre_purpose import normalization
from my_dtw import *
from base_list import *


"""
同一标签，不同距离下的 相位-角度 曲线图
"""
if __name__ == '__main__':
    distances = ['40cm', '50cm']
    # tags = ['B023', 'B022', 'B016']
    tags = ['B023', 'B023']
    # colors = ['blue', 'red', 'black']
    colors = ['red', 'blue']

    bath_dir = 'data/set_four_orientation/distance_'
    similarity_list = []

    freq_i = 0
    for freq in get_freq_list():
        phase_mat = []
        i = 0
        for distance in distances:
            file_path = bath_dir + distance + '/' + 'phase_freq_orientation/' + tags[i] + '.csv'
            data = np.array(pd.read_csv(file_path, header=None))
            # 取第一列数据（功率为24dBm，频率为920.875）
            phase_list = data[:, freq_i]

            # 相位值进行归一化
            phase_list = normalization(phase_list)
            x = [0, 45, 90, 135, 180, 225, 270, 315, 360]
            # 插值法之后的x值
            x_new = np.arange(0, 360, 4.5)
            func = interpolate.interp1d(x, phase_list, kind='cubic')
            y_new = func(x_new)

            phase_mat.append(phase_list)

            plt.plot(x, phase_list, marker='o', markersize=3, color=colors[i], label=distance)
            i += 1

        plt.title("Tag " + tags[0] + "_" + tags[1])
        plt.xlabel("Orientation")
        plt.ylabel("Phase")
        plt.legend()
        plt.show()

        # distance_similarity_origin = TimeSeriesSimilarity(phase_mat[0], phase_mat[1])
        distance_similarity = ImprovedTimeSeriesSimilarity(phase_mat[0], phase_mat[1])
        similarity_list.append(distance_similarity)
        freq_i += 1

    similarity_mean = np.mean(similarity_list)
