import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""
同一距离下，两个标签的 相位-频率-角度 差值热力图
"""
if __name__ == '__main__':
    distance = 'distance_40cm'
    bath_dir = 'phase_time_sequence/set_four_orientation/' + distance + '/phase_freq_orientation/'

    tag1 = 'B016'
    tag2 = 'B023(2)'

    data1 = np.array(pd.read_csv(bath_dir + tag1 + '.csv', header=None))
    data2 = np.array(pd.read_csv(bath_dir + tag2 + '.csv', header=None))

    diff = abs(data1 - data2)

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

    sns.heatmap(diff, cmap='Blues', xticklabels=freq_list, yticklabels=degree_list)

    plt.title('Phase Diff ' + distance + ' ' + tag1 + '&' + tag2)
    plt.xlabel("Freq")
    plt.ylabel("Degree")
    plt.show()

