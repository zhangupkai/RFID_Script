import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from myunwrap import unwrap
from filters import hampel
from pre_purpose import normalization
import seaborn as sns
from base_list import *


if __name__ == '__main__':
    distance = '50cm'
    bath_dir = '../../data/tagPair/distance_' + distance + '/'
    degrees = ['degree_0', 'degree_45', 'degree_90', 'degree_135', 'degree_180',
               'degree_225', 'degree_270', 'degree_315', 'degree_360']
    tag_pair = 'B016_B023'
    tag = 'B016'
    count = '(2)'
    sava_path = 'data/distance_' + distance + '/' + tag_pair + '/' + tag + count + '.csv'
    phase_freq_degree = np.zeros((9, 8))

    # colors = ['red', 'blue', 'green', 'yellow']

    i = 0
    for degree in degrees:
        file_path = bath_dir + '/' + tag_pair + '/' + degree + '/' + tag + count + '_25.0' + '.csv'

        df = pd.read_csv(file_path, header=None, names=['epc', 'freq', 'timestamp', 'phase', 'rssi'])

        # 根据频率并排序
        df.sort_values('freq', ascending=True, inplace=True)
        grouped = df.groupby('freq')

        j = 0
        for name, group in grouped:
            # plt.scatter(group['timestamp'], group['phase'], c=colors[i], alpha=0.6)
            print(name)
            print(group)
            # 当前角度、当前频率下的相位中位数
            phase_median = np.median(np.array(group['phase']))
            phase_freq_degree[i, j] = phase_median
            j += 1

        # 对当前角度下的 相位随频率变化进行unwrap
        phase_freq_degree[i, ] = unwrap(phase_freq_degree[i, ])
        i += 1

    # 归一化
    # phase_freq_degree = normalization(phase_freq_degree)
    sns.heatmap(phase_freq_degree, cmap='Blues', xticklabels=get_freq_list(), yticklabels=get_degree_list())
    plt.title('Phase ' + distance + ' ' + tag + count)
    plt.xlabel("Freq")
    plt.ylabel("Degree")
    plt.show()

    np.savetxt(sava_path, phase_freq_degree, delimiter=',')

