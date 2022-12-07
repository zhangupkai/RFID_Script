import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.interpolate import interpolate
from filters import hampel

# 测试相位随天线面朝方向的变化

tag1 = 'D162'
tag2 = 'D163'

is_inter_deal = True

rotation_level = 'extra_experiment/antenna_tag_90'
count = 50
bath_dir = f'../../data/tagPair/{rotation_level}/{tag1}_{tag2}({count})_32.5.csv'
df = pd.read_csv(bath_dir, header=None, names=['epc', 'freq', 'timestamp', 'phase', 'rssi'])

# 不根据频率分组，全部8个频率下的数据
# 或 不跳频时，单个频率下的数据
# TODO 需要完善，需要间隔的提取两个标签的数据，不能直接根据长度截断
pre_epc = ''
if is_inter_deal is True:
    for index, row in df.iterrows():
        if index == 0:
            pre_epc = row['epc']
            continue
        # 如果当前行的epc等于上一行的epc，删除上一行
        if row['epc'] == pre_epc:
            df = df.drop(index - 1)
        pre_epc = row['epc']

# 根据epc对数据进行分组
grouped = df.groupby('epc')
tag_info1 = np.array(grouped.get_group(tag1))
tag_info2 = np.array(grouped.get_group(tag2))

# 不跳频时，当前频率
freq = tag_info1[0, 1]

tag_info1_size = tag_info1.shape[0]
tag_info2_size = tag_info2.shape[0]

if tag_info1_size > tag_info2_size:
    tag_info1 = tag_info1[:tag_info2_size, :]
elif tag_info1_size < tag_info2_size:
    tag_info2 = tag_info2[:tag_info1_size, :]

timestamp1 = tag_info1[:, 2]
phase1 = tag_info1[:, 3]
timestamp2 = tag_info2[:, 2]
phase2 = tag_info2[:, 3]

# 计算差值并去除异常值
phase_diff = hampel(np.abs(phase1 - phase2))
# phase_diff = np.abs(phase1 - phase2)
# 差值大于PI，减2PI操作
for index in range(len(phase_diff)):
    if phase_diff[index] > math.pi:
        phase_diff[index] -= 2 * math.pi
phase_diff = hampel(np.abs(phase_diff))

phase_diff_interval = np.diff(phase_diff)

# 插值后x轴
timestamp_new = np.linspace(timestamp1[0], timestamp1[timestamp1.shape[0] - 1], timestamp1.shape[0] * 8)

# 数据插值
f = interpolate.interp1d(list(timestamp1), list(phase_diff), kind='slinear', fill_value="extrapolate")
phase_new = f(timestamp_new)

# 组合时间戳和相位差值
phase_time = np.vstack((timestamp_new, phase_new)).T
np.savetxt(f'phase_time_sequence/{rotation_level}/{tag1}_{tag2}({count}).csv', phase_time, delimiter=',')

# plt.title(f'Phase Orientation Time {tag1}_{tag2}_c{count}')
# plt.scatter(x=timestamp1, y=phase_diff, alpha=0.4, s=0.6)
# plt.show()

plt.title(f'Phase Orientation Time Interpolate {tag1}_{tag2}_c{count}')
plt.scatter(x=timestamp_new, y=phase_new, alpha=0.4, s=0.6)
plt.show()
