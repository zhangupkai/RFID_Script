import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from myunwrap import unwrap
from filters import hampel
from pre_purpose import is_phase_hop
import seaborn as sns
from base_list import *
import sys
import math


def deal_data(count):
    distance = '60cm'
    # distance = '50cm_right_10cm'
    bath_dir = '../../data/tagPair/distance_' + distance + '/'
    degrees = ['degree_0', 'degree_45', 'degree_90', 'degree_135', 'degree_180',
               'degree_225', 'degree_270', 'degree_315', 'degree_360']

    tag_pair = 'B016_B023'
    # tag_pair = 'B016_AA03'

    # tag = 'B016'
    tag = 'B023'
    # tag = 'AA03'

    # count = '(1)'
    sava_path = 'data/distance_' + distance + '/' + tag_pair + '/' + tag + count
    phase_freq_degree = np.zeros((9, 8))

    # colors = ['red', 'blue', 'green', 'yellow']

    matplotlib.rcParams.update({'font.size': 12})  # 改变所有字体大小，改变其他性质类似
    i = 0
    for degree in degrees:

        file_path = bath_dir + '/' + tag_pair + '/' + degree + '/' + tag + count + '_25.0' + '.csv'
        print(file_path)
        df = pd.read_csv(file_path, header=None, names=['epc', 'freq', 'timestamp', 'phase', 'rssi'])

        # 当前角度下，如果频率f1下相位发生了跳变并且f1>5，则对f1下的相位减 2PI
        # all_phase = list(df['phase'])
        # print(all_phase)
        # if is_phase_hop(list(df['phase'])):
        #     print(df[df['freq'] == 920.625])
        #     for index, row in df.iterrows():
        #         if (row['freq'] == 920.625) & (row['phase'] > 5):
        #             row['phase'] -= 2 * math.pi
        #             df.at[index, 'phase'] = row['phase']

        # print('---------------')
        # print(df)

        # 根据频率并排序
        df.sort_values('freq', ascending=True, inplace=True)
        # 根据频率分组
        grouped = df.groupby('freq')

        j = 0
        for name, group in grouped:
            # plt.scatter(group['timestamp'], group['phase'], c=colors[i], alpha=0.6)
            print(name)
            print(group)
            # 当前角度下，如果频率f1下相位发生了跳变并且f1>5，则对f1下的相位减 2PI
            # if name == 920.625:
            #     print(is_phase_hop(list(group['phase'])))
            #     if is_phase_hop(list(group['phase'])):
            #         for index, row in group.iterrows():
            #             if row['phase'] > 5:
            #                 row['phase'] -= 2 * math.pi
            #                 group.at[index, 'phase'] = row['phase']

            # 当前角度、当前频率下的相位中位数
            # 先排序，再unwrap，再取中位数
            print(np.array(group['phase']))
            sorted_cur_degree_freq = sorted(np.array(group['phase']))
            print(sorted_cur_degree_freq)
            unwrap_cur_degree_freq = unwrap(sorted(np.array(group['phase'])))
            print(unwrap_cur_degree_freq)
            # sys.exit()

            phase_median = np.median(unwrap(sorted(np.array(group['phase']))))
            # 如果相位大于2PI，减2PI
            # if phase_median > 2 * math.pi:
            #     phase_median -= phase_median
            phase_freq_degree[i, j] = phase_median
            j += 1

        # 对当前角度下的 相位随频率变化进行unwrap
        phase_freq_degree[i, ] = unwrap(phase_freq_degree[i, ])
        i += 1

    # 按列（同一频率，变化角度）unwrap
    # j = 0
    # for col in phase_freq_degree.T:
    #     col = unwrap(col)
    #     phase_freq_degree[:, j] = col
    #     j += 1

    # 归一化
    # phase_freq_degree = normalization(phase_freq_degree)
    sns.heatmap(phase_freq_degree, cmap='Blues', xticklabels=get_freq_list(), yticklabels=get_degree_list())
    plt.title('Phase ' + distance + ' ' + tag + count)
    plt.xlabel("Freq")
    plt.ylabel("Degree")
    plt.xticks(rotation=45)
    plt.yticks(rotation=0)
    # plt.savefig(sava_path + '.png', bbox_inches='tight')
    plt.show()

    np.savetxt(sava_path + '.csv', phase_freq_degree, delimiter=',')


if __name__ == '__main__':
    # counts = ['(1)', '(2)', '(3)', '(4)', '(5)']
    for c in range(1, 16):
        deal_data('(' + str(c) + ')')
