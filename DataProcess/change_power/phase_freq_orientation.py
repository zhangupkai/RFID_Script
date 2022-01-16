import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from myunwrap import *


# 归一化
def normalization(input_data):
    _range = np.max(input_data) - np.min(input_data)
    return (input_data - np.min(input_data)) / _range


"""
得到相位随频率、标签角度变化的数据并画出热力图
"""
if __name__ == '__main__':
    distance = 'distance_50cm'
    degrees = ['degree_0', 'degree_45', 'degree_90', 'degree_135', 'degree_180',
               'degree_225', 'degree_270', 'degree_315', 'degree_360']
    # degrees = ['degree_90']
    # group = 'group4'
    tag = 'B023'
    bath_dir = 'data/set_four_orientation/' + distance + '/'

    # 生成频率列表
    freq_list = []
    for x in range(0, 8):
        freq = 920.625 + x * 0.5
        freq_list.append(freq)

    # 生成角度列表
    degree_list = []
    for x in range(0, 9):
        degree_val = 0 + x * 45
        degree_list.append(degree_val)

    # 9个角度，8个频率
    phase_mat = np.zeros((9, 8))
    i = 0
    for degree in degrees:
        file_path = bath_dir + tag + '_' + degree + '.csv'
        data = np.array(pd.read_csv(file_path, header=None))
        # 取第一行数据（功率为24dBm），并unwarp
        phase_mat[i, :] = unwrap(data[0, :])
        # phase_mat[i, :] = data[0, :]
        i += 1

    # phase_mat_nonzero = phase_mat[np.nonzero(phase_mat)]
    # min_phase = np.min(phase_mat_nonzero)
    # max_phase = np.max(phase_mat_nonzero)
    # print(min_phase, ', ', max_phase)

    # 对相位矩阵进行归一化处理
    normalization_phase_mat = normalization(phase_mat)

    sns.heatmap(normalization_phase_mat, vmin=0, vmax=1, cmap='Blues', xticklabels=freq_list, yticklabels=degree_list)
    plt.title('Phase ' + distance + ' ' + tag)
    plt.xlabel("Freq")
    plt.ylabel("Degree")
    plt.show()

    np.savetxt(bath_dir + 'phase_freq_orientation/' + tag + '.csv', normalization_phase_mat, delimiter=',')
