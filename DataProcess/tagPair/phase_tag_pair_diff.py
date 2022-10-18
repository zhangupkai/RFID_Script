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

from matplotlib import rcParams

# config = {
#     "font.family": 'serif',  # 衬线字体
#     # "font.size": 12,  # 相当于小四大小
#     "font.serif": ['SimSun'],  # 宋体
#     "mathtext.fontset": 'stix',  # matplotlib渲染数学字体时使用的字体，和Times New Roman差别不大
#     'axes.unicode_minus': False  # 处理负号，即-号
# }
# rcParams.update(config)

"""
标签阵列中两个标签的相位差值
"""


def deal_data(count1, count2):
    # distance = '50cm_right_10cm'
    # distance = '40cm'
    # distance = '60cm_left_18cm'
    # distance = 'vertical'

    tag_pair = 'B034_B029'
    tag1 = 'B034'
    tag2 = 'B029'

    # tag_pair = 'B018_B023'
    # tag1 = 'B018'
    # tag2 = 'B023'

    # tag_pair = 'B018_AA03'
    # tag1 = 'B018'
    # tag2 = 'AA03'

    # tag_pair = 'F001_F005'
    # tag1 = 'F001'
    # tag2 = 'F005'

    # tag_pair = 'E002_E006'
    # tag1 = 'E002'
    # tag2 = 'E006'

    # tag_pair = 'E002_C001'
    # tag1 = 'E002'
    # tag2 = 'C001'

    # tag_pair = 'F001_E006'
    # tag1 = 'F001'
    # tag2 = 'E006'

    # tag_pair = 'F002_F003'
    # tag1 = 'F002'
    # tag2 = 'F003'

    # tag_pair = 'C001_C002'
    # tag1 = 'C001'
    # tag2 = 'C002'

    # tag_pair = 'C003_C004'
    # tag1 = 'C003'
    # tag2 = 'C004'

    # tag_pair = 'E004_E005'
    # tag1 = 'E004'
    # tag2 = 'E005'

    # count = '(2)'
    bath_dir = 'data/fixed_degree/' + tag_pair + '/'
    degrees = ['degree_0', 'degree_45', 'degree_90', 'degree_135', 'degree_180',
               'degree_225', 'degree_270', 'degree_315', 'degree_360']
    # sava_path = 'phase_time_sequence/distance_' + distance + '/' + tag_pair + '/' + tag_pair + count1 + count2
    sava_path = f'data/dataset/{tag_pair}/{tag_pair}{count1}{count2}'
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

    # matplotlib.rcParams.update({'font.size': 18})  # 改变所有字体大小，改变其他性质类似

    # plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 用来正常显示中文标签
    # plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

    plt.rc('font', family='Times New Roman', size=18, weight='bold')

    ax = sns.heatmap(phase_diff, cmap='Blues', xticklabels=get_freq_list(),
                     yticklabels=['0', 'π/4', 'π/2', '3π/4', 'π', '5π/4', '3π/2', '7π/4', '2π'])
    # plt.title('Phase Diff ' + '' + ' ' + tag_pair + " " + count1 + count2)

    label_font = {
        'size': 18,
        'weight': 'bold',
        'family': 'SimSun'
    }

    # plt.xlabel("Frequency (MHz)", fontdict=label_font)
    # plt.ylabel("Angle (Rad)", fontdict=label_font)
    plt.xlabel("载波频率（MHz）", fontdict=label_font)
    plt.ylabel("标签角度（Rad）", fontdict=label_font)
    plt.xticks(rotation=45, size=18, weight='bold', family='Times New Roman')
    plt.yticks(rotation=0, size=18, weight='bold', family='Times New Roman')

    # 设置colorbar的刻度字体大小
    cax = plt.gcf().axes[-1]
    cax.tick_params(labelsize=16)
    # 设置colorbar的label文本和字体大小
    cbar = ax.collections[0].colorbar
    bar_font = {
        'size': 18,
        'weight': 'bold',
        'family': 'SimSun'
        # 'family': 'Times New Roman'
    }
    # cbar.set_label('Phase Difference (Rad)', fontdict=bar_font, labelpad=8.5)
    cbar.set_label('相位差分（Rad）', fontdict=bar_font, labelpad=8.5)

    # plt.savefig('D:/Graduate/Paper Writing/matlab/my_code/fig/matrix.pdf', bbox_inches='tight', dpi=600, format='pdf')
    # plt.savefig('D:/Graduate/Paper Writing/matlab/my_code/fig/matrix.png', bbox_inches='tight')
    plt.savefig('D:/Graduate/Paper Writing/大论文/Figure/3_特征矩阵.png', bbox_inches='tight', dpi=600)
    plt.show()

    np.savetxt(sava_path + '.csv', phase_diff, delimiter=',')


if __name__ == '__main__':
    # counts = ['(1)', '(2)', '(3)', '(4)', '(5)']
    for c1 in range(1, 2):
        for c2 in range(1, 2):
            deal_data('({c1})'.format(c1=c1), '({c2})'.format(c2=c2))
