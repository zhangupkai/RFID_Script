import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from myunwrap import unwrap
from filters import hampel
from pre_purpose import normalization
import seaborn as sns
from base_list import *
import math

"""
标签阵列中两个标签的相位差值
"""


def deal_data(count1, count2):
    # distance = '50cm_right_10cm'
    # distance = '40cm'
    # distance = '60cm_left_20cm'
    # distance = 'vertical'

    tag_pair = 'B034_B029'
    tag1 = 'B034'
    tag2 = 'B029'

    # tag_pair = 'B016_B023'
    # tag1 = 'B016'
    # tag2 = 'B023'

    # tag_pair = 'B016_AA03'
    # tag1 = 'B016'
    # tag2 = 'AA03'

    # count = '(2)'
    bath_dir = 'data/fixed_degree/' + tag_pair + '/'
    degrees = ['degree_0', 'degree_45', 'degree_90', 'degree_135', 'degree_180',
               'degree_225', 'degree_270', 'degree_315', 'degree_360']
    # sava_path = 'phase_time_sequence/distance_' + distance + '/' + tag_pair + '/' + tag_pair + count1 + count2
    sava_path = f'data/dataset/{tag_pair}/fixed_degree/{tag_pair}{count1}{count2}'
    phase_freq_degree = np.zeros((9, 8))

    file_path1 = bath_dir + tag1 + count1 + '.csv'
    file_path2 = bath_dir + tag2 + count2 + '.csv'
    data1 = pd.read_csv(file_path1, header=None)
    data2 = pd.read_csv(file_path2, header=None)

    phase_diff = np.abs(data1 - data2)
    # 差值大于PI，减2PI操作
    for phase in np.nditer(phase_diff, op_flags=['readwrite']):
        if phase > math.pi:
            phase -= 2 * math.pi
    phase_diff = np.abs(phase_diff)

    matplotlib.rcParams.update({'font.size': 12})  # 改变所有字体大小，改变其他性质类似

    sns.heatmap(phase_diff, cmap='Blues', xticklabels=get_freq_list(), yticklabels=get_degree_list())
    plt.title('Phase Diff ' + '' + ' ' + tag_pair + " " + count1 + count2)
    plt.xlabel("Freq")
    plt.ylabel("Degree")
    plt.xticks(rotation=45)
    plt.yticks(rotation=0)
    # plt.savefig(sava_path + '.png', bbox_inches='tight')
    plt.show()

    np.savetxt(sava_path + '.csv', phase_diff, delimiter=',')


if __name__ == '__main__':
    # counts = ['(1)', '(2)', '(3)', '(4)', '(5)']
    for c1 in range(2, 16):
        for c2 in range(2, 16):
            deal_data('({c1})'.format(c1=c1), '({c2})'.format(c2=c2))
