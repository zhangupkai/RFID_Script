import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from myunwrap import unwrap
from filters import hampel
from pre_purpose import normalization
import seaborn as sns
from base_list import *


"""
两个不同的标签阵列的相位差值
"""
if __name__ == '__main__':
    distance = '60cm'
    tag_pair = 'TagPair A & B'
    # tag1 = 'B016'
    # tag2 = 'B023'
    count = ''
    bath_dir = 'phase_time_sequence/distance_' + distance + '/' + tag_pair + '/'
    degrees = ['degree_0', 'degree_45', 'degree_90', 'degree_135', 'degree_180',
               'degree_225', 'degree_270', 'degree_315', 'degree_360']
    sava_path = 'phase_time_sequence/distance_' + distance + '/' + tag_pair + '/' + tag_pair + '.csv'
    phase_freq_degree = np.zeros((9, 8))

    file_path1 = 'data/distance_60cm/B016_AA03/B016_AA03.csv'
    file_path2 = 'data/distance_60cm/B016_B023/B016_B023.csv'
    data1 = pd.read_csv(file_path1, header=None)
    data2 = pd.read_csv(file_path2, header=None)

    phase_diff = np.abs(data1 - data2)

    matplotlib.rcParams.update({'font.size': 12})  # 改变所有字体大小，改变其他性质类似

    sns.heatmap(phase_diff, cmap='Blues', xticklabels=get_freq_list(), yticklabels=get_degree_list())
    plt.title('Phase Diff ' + distance + ' ' + tag_pair + " " + count)
    plt.xlabel("Freq")
    plt.ylabel("Degree")

    plt.show()

    # np.savetxt(sava_path, phase_diff, delimiter=',')
