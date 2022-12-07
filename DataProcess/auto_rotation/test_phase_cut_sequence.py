import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.interpolate import interpolate
from filters import hampel

# 测试相位随天线面朝方向的变化曲线，滑动窗口截取出有效段

tag1 = 'D162'
tag2 = 'D163'

rotation_level = 'extra_experiment/antenna_tag_90'
count = 50

bath_dir = f'phase_time_sequence/{rotation_level}/{tag1}_{tag2}({count}).csv'
df = pd.read_csv(bath_dir, header=None, names=['timestamp', 'phase_diff'])

# 滑动窗口，窗口长度1000
roll_window = df.rolling(window=1000)
# 每个窗口内数据的标准差
roll_std = roll_window.std()
# 有效时间序列的起始和终止标准差阈值
threshold_l = 0.03
threshold_r = 0.03

start_index = 0
end_index = 0
for index, row in roll_std.iterrows():
    if row['phase_diff'] > threshold_l:
        start_index = index
        print(start_index)
        break

# roll_std 倒序
roll_std_reverse = roll_std.iloc[::-1]
for index, row in roll_std_reverse.iterrows():
    if row['phase_diff'] > threshold_r:
        end_index = index
        print(end_index)
        break

# 有效时间序列
df_valid = df[start_index:end_index+1]
# 天线正对着标签的时刻 t ==> 相位差值最小的时刻
idx_min = df_valid['phase_diff'].idxmin()
# 时刻 t 在整个天线改变朝向的过程所处于的时间位置
res_proportion = idx_min / (end_index - start_index + 1)
res = 45 + 90 * res_proportion
res_err = abs(res - 90)
