import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def condition_1_hop_freq():
    x_c1 = ['not hop', 'hop when rotation', 'hop after rotation']
    y_c1 = [1.0, 0.9792, 1.0]

    # plt.figure(figsize=(4, 4))
    plt.bar(x=x_c1, height=y_c1, width=0.4)

    for _x, _y in zip(x_c1, y_c1):
        plt.text(_x, _y + 0.01, str(_y), ha='center', va='bottom', fontsize=10, rotation=0)

    plt.title('Condition 1: Hop Freq')
    plt.xlabel('Hop')
    plt.ylabel('Accuracy')
    plt.show()


def condition_2_rotation_level():
    x_c1 = ['level 1', 'level 2', 'level 3']
    y_c1 = [0.875, 0.8512, 0.845]

    # plt.figure(figsize=(4, 4))
    plt.bar(x=x_c1, height=y_c1, width=0.4)
    plt.plot(x_c1, y_c1, c='red', marker='^')

    for _x, _y in zip(x_c1, y_c1):
        plt.text(_x, _y + 0.01, str(_y), ha='center', va='bottom', fontsize=10, rotation=0)

    plt.ylim((0, 1))
    plt.title('Condition 2: Rotation Level')
    plt.xlabel('Rotation Level')
    plt.ylabel('Accuracy')
    plt.show()


def condition_3_object_distance():
    x_data = ['75cm', '85cm', '100cm']
    x = np.arange(3)
    acc_1 = np.array([97.06, 94.67, 95.24])
    acc_0 = np.array([99.26, 98.07, 98.73])
    # acc_t = [98.82, 97.17, 98.00]

    total_width, n = 0.6, 2  # 柱状图总宽度，有几组数据
    width = total_width / n  # 单个柱状图的宽度
    x1 = x - width / 2  # 第一组数据柱状图横坐标起始位置
    x2 = x1 + width  # 第二组数据柱状图横坐标起始位置

    # plt.figure(figsize=(4, 4))
    plt.bar(x=x1, height=acc_1, width=width, label='Legal Tag')
    plt.bar(x=x2, height=acc_0, width=width, label='Illegal Tag')
    # plt.plot(x_c1, y_c1, c='red', marker='^')

    for _x, _y in zip(x1, acc_1):
        plt.text(_x, _y + 0.01, str(_y), ha='center', va='bottom', fontsize=10, rotation=0)

    for _x, _y in zip(x2, acc_0):
        plt.text(_x, _y + 0.01, str(_y), ha='center', va='bottom', fontsize=10, rotation=0)

    plt.xticks(x, x_data)

    plt.ylim((0, 105))
    plt.title('Condition 1: Object Distance')
    plt.xlabel('Object Distance')
    plt.ylabel('Accuracy(%)')
    plt.legend(loc='lower right')
    plt.show()


def condition_5_tag_type():
    x_c1 = ['type 1', 'type 2']
    y_c1 = [1.0, 0.8347]

    # plt.figure(figsize=(4, 4))
    plt.bar(x=x_c1, height=y_c1, width=0.4)

    for _x, _y in zip(x_c1, y_c1):
        plt.text(_x, _y + 0.01, str(_y), ha='center', va='bottom', fontsize=10, rotation=0)

    plt.title('Condition 5: Tag Type')
    plt.xlabel('Tag Type')
    plt.ylabel('Accuracy')
    plt.show()


def condition_6_interfer_tag_numbers():
    x_data = ['0 tag', '20 tags', '40 tags', '60 tags']
    x = np.arange(4)

    acc_1 = np.array([97.06, 86.67, 82.35, 76.19])
    acc_0 = np.array([99.26, 94.12, 90.62, 84.38])

    total_width, n = 0.6, 2  # 柱状图总宽度，有几组数据
    width = total_width / n  # 单个柱状图的宽度
    x1 = x - width / 2  # 第一组数据柱状图横坐标起始位置
    x2 = x1 + width  # 第二组数据柱状图横坐标起始位置

    # plt.figure(figsize=(4, 4))
    plt.bar(x=x1, height=acc_1, width=width, label='Legal Tag')
    plt.bar(x=x2, height=acc_0, width=width, label='Illegal Tag')
    # plt.plot(x_c1, y_c1, c='red', marker='^')

    for _x, _y in zip(x1, acc_1):
        plt.text(_x, _y + 0.01, str(_y), ha='center', va='bottom', fontsize=10, rotation=0)

    for _x, _y in zip(x2, acc_0):
        plt.text(_x, _y + 0.01, str(_y), ha='center', va='bottom', fontsize=10, rotation=0)

    plt.ylim(0, 105)
    plt.xticks(x, x_data)
    plt.title('Condition 3: Interfering Tag Numbers')
    plt.xlabel('Interfering Tag Numbers')
    plt.ylabel('Accuracy(%)')
    plt.legend(loc='lower right')
    plt.show()


if __name__ == '__main__':
    condition_6_interfer_tag_numbers()
