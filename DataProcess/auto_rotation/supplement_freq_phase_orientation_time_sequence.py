import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import interpolate
from filters import hampel
from base_list import get_freq_list
from locate_degree_main import locate_degree

# 补全单个频率下的 相位-角度-时间序列
# TODO 去除离群值 插值

# tag1 = 'B034'
# tag2 = 'B029'
# tag1 = 'B016'
# tag2 = 'AA03'
# tag1 = 'B016'
# tag2 = 'B023'
# tag1 = 'E002'
# tag2 = 'E006'
tag1 = 'F001'
tag2 = 'F005'
# tag1 = 'E002'
# tag2 = 'C001'

# 转动周期，微秒级
# circle_time = 108520704

rotation_level = 'final_experiment/1_hop'
rotation_level_abbr = '_c1_hop'

# 最终得到的相位矩阵，9个角度（9行），8个频率（8列）
phase_mat = np.zeros((9, 8))

for count in range(11, 16):
    col = 0
    # for freq in [920.625]:
    for freq in get_freq_list():
        bath_dir = f'phase_time_sequence/{rotation_level}/{tag1}_{tag2}({count})_{freq}.csv'
        data = np.array(pd.read_csv(bath_dir, header=None))
        timestamp = data[:, 0]
        phase = data[:, 1]
        # phase_timestamp = dict(zip(timestamp, phase))
        # size = timestamp.shape[0]

        # 去除异常值
        phase_after = hampel(phase)

        """
        # TODO 提取特征点之前 - 根据周期补全数据
        #
        to_append_dict = {}
        for key_timestamp, value_phase in phase_timestamp.items():
            # 当前是第几个周期（从第0个开始）
            cur_circle = (key_timestamp - timestamp[0]) // circle_time
            # print('cur circle: ', cur_circle)
            if cur_circle == 1:
                to_append_dict[key_timestamp - circle_time * cur_circle] = value_phase
    
        # 从第二个周期开始的数据补充第一个周期内的数据
        phase_timestamp.update(to_append_dict)
        # 字典中的数据按照时间戳顺序再进行一次升序排序
        sorted(phase_timestamp.keys())
    
        plt.title(f'Phase Orientation Time (Tag Pair freq_{freq} {tag1}_{tag2}_c{count})')
        plt.scatter(x=phase_timestamp.keys(), y=phase_timestamp.values(), alpha=0.4, s=0.6)
        plt.show()
        """

        # 时间戳间隔
        timestamp_interval = []
        for index in range(timestamp.shape[0]):
            if index > 0:
                timestamp_interval.append(timestamp[index] - timestamp[index - 1])

        timestamp_interval = np.array(timestamp_interval)
        # plt.title("Timestamp Interval")
        # plt.scatter(x=np.arange(0, timestamp_interval.shape[0], 1), y=timestamp_interval, alpha=0.4, s=0.6)
        # plt.show()

        # 时间戳间隔的阈值，大于阈值说明时间戳发生跳变
        TIME_INTER_THRESHOLD = 10000000
        # timestamp_interval数组中大于阈值的索引
        exceed_time_inter_idx = np.where(timestamp_interval > TIME_INTER_THRESHOLD)[0]

        # 根据时间戳的跳变，对时间戳和相位数据进行分段（一个段为图中的一个竖条数据）
        split_timestamp = np.split(timestamp, exceed_time_inter_idx + 1)
        split_phase = np.split(phase_after, exceed_time_inter_idx + 1)
        # 每一段数据取其中位数作为特征点
        split_timestamp_median = []
        split_phase_median = []
        for index in range(len(split_phase)):
            split_phase_median.append(np.median(split_phase[index]))
            split_timestamp_median.append(np.median(split_timestamp[index]))

        plt.title('Phase Orientation Time (Extract Feature Point)')
        plt.scatter(x=split_timestamp_median, y=split_phase_median, alpha=0.8, s=10)
        plt.show()

        """
        # TODO Start 对特征提取之后的数据点 依据周期进行数据补充
        phase_timestamp = dict(zip(split_timestamp_median, split_phase_median))
        # 需要在添加到phase_timestamp字典中的数据
        to_append_dict = {}
        # 第一个数据点所处的时间戳
        start_timestamp = split_timestamp_median[0]
        # 判断这一组数据一共历经了几个周期(circle_time)
        T_sum = int((split_timestamp_median[len(split_timestamp_median) - 1] - start_timestamp) // circle_time + 1)
        for k_timestamp, v_phase in phase_timestamp.items():
            # 当前数据点属于第几个周期（下标从0开始）
            T_cur = int((k_timestamp - start_timestamp) // circle_time)
            # 将数据点复制到其余周期中
            for T_iter in range(0, T_sum):
                if T_iter == T_cur:
                    continue
                to_append_dict[k_timestamp + (T_iter - T_cur) * circle_time] = v_phase
    
        # 将to_append_dict中的数据加入到phase_timestamp字典中
        phase_timestamp.update(to_append_dict)
    
        plt.title('Phase Orientation Time (Add Periodic Feature)')
        plt.scatter(x=phase_timestamp.keys(), y=phase_timestamp.values(), alpha=0.8, s=8)
        plt.show()
    
        # TODO End 对特征提取之后的数据点 依据周期进行数据补充
        """

        # 插值后x轴，时间戳轴长度*8 Because: 一共8个频率数据
        timestamp_new = np.linspace(timestamp[0], timestamp[timestamp.shape[0] - 1], timestamp.shape[0] * 8)

        # print('k:', list(phase_timestamp.keys()), ' v:', list(phase_timestamp.values()))
        # 数据插值
        f = interpolate.interp1d(split_timestamp_median, split_phase_median, kind='cubic', fill_value="extrapolate")
        phase_new = f(timestamp_new)
        plt.title(f'Phase Orientation Time (Interpolation) {tag1}_{tag2} c{count}')
        plt.scatter(x=split_timestamp_median, y=split_phase_median, alpha=0.8, s=10)
        plt.plot(timestamp_new, phase_new)
        plt.show()

        # 单个频率下，在相位角度时间序列中定位到指定的9个角度
        phase_orientation = locate_degree(timestamp_new, phase_new, f'{tag1}_{tag2}', freq)
        phase_mat[:, col] = np.array(phase_orientation)
        col += 1

    save_path = f'{rotation_level}/{tag1}_{tag2}/{tag1}_{tag2}{rotation_level_abbr}({count}).csv'
    np.savetxt(save_path, phase_mat, delimiter=',')
