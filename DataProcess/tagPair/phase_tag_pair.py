import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from myunwrap import unwrap
from filters import hampel
from pre_purpose import deal_zero_phase
import seaborn as sns
from base_list import *
import sys
import math


def deal_data(count):
# if __name__ == '__main__':
#     count = '(2)'
    # distance = '70cm'
    # distance = '50cm_right_10cm'
    # distance = '60cm_left_20cm'
    # distance = '40cm'
    # distance = 'vertical'
    bath_dir = '../../data/tagPair/fixed_degree/'
    degrees = ['degree_0', 'degree_45', 'degree_90', 'degree_135', 'degree_180',
               'degree_225', 'degree_270', 'degree_315', 'degree_360']

    # tag_pair = 'B034_B029'
    # tag_pair = 'B016_AA03'
    # tag_pair = 'B016_B023'
    # tag_pair = 'F001_F005'
    # tag_pair = 'E002_E006'
    # tag_pair = 'E002_C001'
    # tag_pair = 'F001_E006'
    # tag_pair = 'F002_F003'
    # tag_pair = 'C001_C002'
    # tag_pair = 'C003_C004'
    tag_pair = 'E004_E005'

    tag = 'E005'

    # count = '(1)'
    sava_path = 'data/fixed_degree/' + tag_pair + '/' + tag + count
    phase_freq_degree = np.zeros((9, 8))

    # colors = ['red', 'blue', 'green', 'yellow']

    matplotlib.rcParams.update({'font.size': 12})  # 改变所有字体大小，改变其他性质类似

    # 角度index
    i = 0
    for degree in degrees:
        file_path = bath_dir + '/' + tag_pair + '/' + degree + '/' + tag_pair + count + '_25.0' + '.csv'
        # print(file_path)
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

        # 筛选指定epc
        df = df[df['epc'] == tag]
        # 根据频率并排序
        df.sort_values('freq', ascending=True, inplace=True)
        # 根据频率分组
        grouped = df.groupby('freq')

        # 频率index
        j = 0
        # TODO 有的频率没有跳到，固定的几个分组是否都有，没有的话需要进行进一步操作
        for freq in get_freq_list():
            # 正常跳到的频率
            if freq in grouped.groups:
                group = grouped.get_group(freq)
                # 当前角度、当前频率下的相位中位数
                # 先排序，再unwrap，再取中位数
                sorted_cur_degree_freq = sorted(np.array(group['phase']))
                unwrap_cur_degree_freq = unwrap(sorted_cur_degree_freq)
                phase_median = np.median(unwrap_cur_degree_freq)
                phase_freq_degree[i, j] = phase_median
            j += 1

        # 对当前角度下 处理相位零值情况
        phase_freq_degree[i, ] = deal_zero_phase(phase_freq_degree[i, ])
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
    plt.title('Phase ' + '' + ' ' + tag + count)
    plt.xlabel("Freq")
    plt.ylabel("Degree")
    plt.xticks(rotation=45)
    plt.yticks(rotation=0)
    # plt.savefig(sava_path + '.png', bbox_inches='tight')
    plt.show()

    np.savetxt(sava_path + '.csv', phase_freq_degree, delimiter=',')


if __name__ == '__main__':
    # counts = ['(1)', '(2)', '(3)', '(4)', '(5)']
    for c in range(1, 6):
        deal_data('(' + str(c) + ')')
