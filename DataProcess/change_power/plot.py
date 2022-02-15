import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import sys
import os


def phase_heat():
    distance = 'distance_50cm'
    degree = 'degree_180'
    group = 'group1_'
    group_name = 'Group1 '
    tag = 'B023'
    phase_mat = np.array(
        pd.read_csv('phase_time_sequence/set_four_orientation/' + distance + '/' + tag + '_' + degree + '.csv', header=None))

    phase_mat_nonzero = phase_mat[np.nonzero(phase_mat)]
    min_phase = np.min(phase_mat_nonzero)
    max_phase = np.max(phase_mat_nonzero)
    print(min_phase, ', ', max_phase)

    # 去除0值
    pre_phase = 0.0
    for i in range(0, 12):
        for j in range(0, 16):
            # if phase_mat[i, j] == 0.0:
            phase_mat[i, j] = phase_mat[i, j]
            # pre_phase = phase_mat[i, j]

    # 生成功率列表
    power_list = []
    for x in range(0, 12):
        power = 20 + x
        power_list.append(power)

    # 生成频率列表
    freq_list = []
    for x in range(0, 16):
        freq = 920.625 + x * 0.25
        freq_list.append(freq)

    # 作图阶段
    # fig = plt.figure()
    # 定义画布为1*1，在第1个位置作图
    # ax = fig.add_subplot(111)
    # 定义横纵坐标的刻度
    # ax.set_xticks(range(len(power_list)))
    # ax.set_xticklabels(power_list)
    # ax.set_yticks(range(len(freq_list)))
    # ax.set_yticklabels(freq_list)
    # 作图并选择热图的颜色填充风格，这里选择hot
    # im = ax.imshow(phase_mat, cmap=plt.cm.hot_r)
    # 增加右侧的颜色刻度条
    # plt.colorbar(im)
    # 增加标题
    # plt.title("Phase_Power_Freq A991")
    # show
    # plt.show()
    sns.set(font_scale=0.8)
    plt.rc('font', size=12)
    sns.heatmap(phase_mat, vmin=min_phase, vmax=max_phase, cmap='Blues', xticklabels=freq_list, yticklabels=power_list)
    plt.title('Phase ' + distance + ' ' + tag + ' ' + degree)
    # plt.savefig('phase_time_sequence/set_four_orientation/' + distance + '/' + tag + '_' + degree + '.jpg')
    plt.show()


def diff_tag():
    phase_mat = np.array(pd.read_csv('data/set_two_25-30/group6.csv', header=None))
    # 生成功率列表
    power_list = []
    for x in range(0, 21):
        power = 25.0 + x * 0.25
        power_list.append(power)

    plt.title('Group6 Phase-Power')
    plt.plot(power_list, phase_mat[0, :], label='A991')
    plt.plot(power_list, phase_mat[1, :], label='A992', color='r')
    plt.plot(power_list, phase_mat[2, :], label='A993', color='b')
    plt.plot(power_list, phase_mat[3, :], label='A994', color='g')
    plt.plot(power_list, phase_mat[4, :], label='A995', color='k')
    plt.legend()
    plt.show()


def same_tag():
    group1 = np.array(pd.read_csv('data/set_one_20-30/group1.csv', header=None))
    group2 = np.array(pd.read_csv('data/set_one_20-30/group2.csv', header=None))
    group3 = np.array(pd.read_csv('data/set_one_20-30/group3.csv', header=None))
    group4 = np.array(pd.read_csv('data/set_one_20-30/group4.csv', header=None))
    group5 = np.array(pd.read_csv('data/set_one_20-30/group5.csv', header=None))
    phase_mat = np.zeros((5, 11))
    # 取A991数据
    phase_mat[0, :] = group1[0, :]
    phase_mat[1, :] = group2[0, :]
    phase_mat[2, :] = group3[0, :]
    phase_mat[3, :] = group4[0, :]
    phase_mat[4, :] = group5[0, :]

    power = range(20, 31)
    plt.title("A991 Phase-Power")
    plt.plot(power, phase_mat[0, :], label='group1')
    plt.plot(power, phase_mat[1, :], label='group2', color='r')
    plt.plot(power, phase_mat[2, :], label='group3', color='b')
    plt.plot(power, phase_mat[3, :], label='group4', color='g')
    plt.plot(power, phase_mat[4, :], label='group5', color='k')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    phase_heat()
    # diff_tag()
    # same_tag()
