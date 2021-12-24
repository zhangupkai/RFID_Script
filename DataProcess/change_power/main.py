import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# 欧式距离
def cal_distance(s1, s2):
    m = len(s1)
    n = len(s2)
    plt.plot(s1, "r", s2, "g")
    plt.show()
    s1 = (s1 - np.mean(s1)) / np.std(s1)
    s2 = (s2 - np.mean(s2)) / np.std(s2)
    distance = 0
    for i in range(m):
        distance += (s1[i] - s2[i]) ** 2
    return np.sqrt(distance)


# DTW
def TimeSeriesSimilarity(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    # plt.plot(s1, "r", s2, "g")
    plt.show()
    s1 = (s1 - np.mean(s1)) / np.std(s1)
    s2 = (s2 - np.mean(s2)) / np.std(s2)
    paths = np.full((l1 + 1, l2 + 1), np.inf)  # 全部赋予无穷大
    paths[0, 0] = 0
    for i in range(l1):
        for j in range(l2):
            d = s1[i] - s2[j]
            cost = d ** 2
            paths[i + 1, j + 1] = cost + min(paths[i, j + 1], paths[i + 1, j], paths[i, j])

    paths = np.sqrt(paths)
    s = paths[l1, l2]
    return s, paths.T


def sameTagDiffPower():
    data_30 = np.array(pd.read_csv('../../data/changePower/changePowerA991_30.0_group2.csv'))
    data_25 = np.array(pd.read_csv('../../data/changePower/changePowerA991_25.0_group2.csv'))
    data_20 = np.array(pd.read_csv('../../data/changePower/changePowerA991_20.0_group2.csv'))

    x_len = min(len(data_30[:, 2]), len(data_25[:, 2]), len(data_20[:, 2]))
    x = range(x_len - 1)
    # x1 = range(len(data_30[:, 2]))
    y1 = data_30[:x_len - 1, 3]
    # x2 = range(len(data_25[:, 2]))
    y2 = data_25[:x_len - 1, 3]
    # x3 = range(len(data_20[:, 2]))
    y3 = data_20[:x_len - 1, 3]

    # distance1_2 = cal_distance(y1, y2)
    # distance1_3 = cal_distance(y1, y3)
    # distance2_3 = cal_distance(y2, y3)
    distance1_2, _ = TimeSeriesSimilarity(y1, y2)
    distance1_3, _ = TimeSeriesSimilarity(y1, y3)
    distance2_3, _ = TimeSeriesSimilarity(y2, y3)

    plt.title("Tag A991 Group1")
    plt.plot(x, y1, label='30dBm')
    plt.plot(x, y2, color='r', label='25dBm')
    plt.plot(x, y3, color='b', label='20dBm')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    data_A991 = np.array(pd.read_csv('../../data/changePower/changePowerA991_30.0.csv'))
    data_A993 = np.array(pd.read_csv('../../data/changePower/changePowerA993_30.0.csv'))
    data_A995 = np.array(pd.read_csv('../../data/changePower/changePowerA995_30.0.csv'))

    x_len = min(len(data_A991[:, 2]), len(data_A993[:, 2]), len(data_A995[:, 2]))
    x = range(x_len - 1)
    # x1 = range(len(data_30[:, 2]))
    y1 = data_A991[:x_len - 1, 3]
    # x2 = range(len(data_25[:, 2]))
    y2 = data_A993[:x_len - 1, 3]
    # x3 = range(len(data_20[:, 2]))
    y3 = data_A995[:x_len - 1, 3]

    # distance1_2 = cal_distance(y1, y2)
    # distance1_3 = cal_distance(y1, y3)
    # distance2_3 = cal_distance(y2, y3)
    distance1_2, _ = TimeSeriesSimilarity(y1, y2)
    distance1_3, _ = TimeSeriesSimilarity(y1, y3)
    distance2_3, _ = TimeSeriesSimilarity(y2, y3)

    plt.title("30dBm Group1")
    plt.plot(x, y1, label='A991')
    plt.plot(x, y2, color='r', label='A993')
    plt.plot(x, y3, color='b', label='A995')
    plt.legend()
    plt.show()
