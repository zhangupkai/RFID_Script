import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys
import os

if __name__ == '__main__':
    tags = ['A991', 'A992', 'A993', 'A994', 'A995']
    bath_dir = '../../data/changePower2/SetTwo25-30dBm/group6/'

    # 生成功率列表
    power_list = []
    for x in range(0, 21):
        power = 25.0 + x * 0.25
        power_list.append(power)

    phase_mat = np.zeros((5, 21))
    i = 0
    for tag in tags:
        j = 0
        for power in power_list:
            # power = 25.0 + power_index * 0.25
            file_path = bath_dir + tag + '/changePower2' + tag + '_' + str(power) + '.csv'
            print(file_path)
            if os.stat(file_path).st_size > 0:
                data = np.array(pd.read_csv(file_path, header=None))
                # 相位均值
                phase = np.mean(data[:, 3])
                print(phase)
                phase_mat[i, j] = phase
            j += 1
        i += 1

    np.savetxt('data/set_two_25-30/group6.csv', X=phase_mat, delimiter=',')

    plt.title('Phase-Power')
    plt.plot(power_list, phase_mat[0, :], label='A991')
    plt.plot(power_list, phase_mat[1, :], label='A992', color='r')
    plt.plot(power_list, phase_mat[2, :], label='A993', color='b')
    plt.plot(power_list, phase_mat[3, :], label='A994', color='g')
    plt.plot(power_list, phase_mat[4, :], label='A995', color='k')
    plt.legend()
    plt.show()

    # data_A991 = np.array(pd.read_csv('../../data/changePower/changePowerA991_30.0.csv'))
    # data_A993 = np.array(pd.read_csv('../../data/changePower/changePowerA993_30.0.csv'))
    # data_A995 = np.array(pd.read_csv('../../data/changePower/changePowerA995_30.0.csv'))
    #
    # x_len = min(len(data_A991[:, 2]), len(data_A993[:, 2]), len(data_A995[:, 2]))
    # x = range(x_len - 1)
    # # x1 = range(len(data_30[:, 2]))
    # y1 = data_A991[:x_len - 1, 3]
    # # x2 = range(len(data_25[:, 2]))
    # y2 = data_A993[:x_len - 1, 3]
    # # x3 = range(len(data_20[:, 2]))
    # y3 = data_A995[:x_len - 1, 3]
    #
    # plt.title("30dBm Group1")
    # plt.plot(x, y1, label='A991')
    # plt.plot(x, y2, color='r', label='A993')
    # plt.plot(x, y3, color='b', label='A995')
    # plt.legend()
    # plt.show()
