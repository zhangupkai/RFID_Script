import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from utils import myunwrap
from matplotlib.ticker import MultipleLocator, FixedLocator
from matplotlib.font_manager import FontProperties

# font = FontProperties(fname='C:\Windows\Fonts\Microsoft YaHei UI')
from matplotlib import rcParams

config = {
    "font.family": 'serif',  # 衬线字体
    # "font.size": 12,  # 相当于小四大小
    "font.serif": ['SimSun'],  # 宋体
    "mathtext.fontset": 'stix',  # matplotlib渲染数学字体时使用的字体，和Times New Roman差别不大
    'axes.unicode_minus': False  # 处理负号，即-号
}
rcParams.update(config)

bath_dir = 'D:/Coding/RFID/RFID_Script/data/tagPair/final_experiment/2_rotation_level/level_2/C001_C002/' \
           'C001_C002(1)_25.0.csv'

bath_dir_distance = 'D:/Coding/RFID/RFID_Script/data/tagPair/final_experiment/3_object_distance/distance_2/C001_C002/' \
                    'C001_C002(1)_25.0.csv'

tag_pair_type = 3
tag1 = 'C001'
tag2 = 'C002'

df = pd.read_csv(bath_dir, header=None, names=['epc', 'freq', 'timestamp', 'phase', 'rssi'])
df_distance = pd.read_csv(bath_dir_distance, header=None, names=['epc', 'freq', 'timestamp', 'phase', 'rssi'])

grouped = df.groupby('epc')
grouped_2 = df_distance.groupby('epc')

data1 = np.array(grouped.get_group(tag1))
# data2 = np.array(grouped.get_group(tag2))
data2 = np.array(grouped_2.get_group(tag1))

timestamp1 = data1[:, 2]
phase1 = data1[:, 3]
phase1 = myunwrap.unwrap(phase1)

timestamp2 = data2[:, 2]
phase2 = data2[:, 3]
phase2 = myunwrap.unwrap(phase2)
# print(phase[15851])

timestamp_diff = timestamp2[0] - timestamp1[0]
timestamp2 = timestamp2 - timestamp_diff

timestamp1 = timestamp1[:len(timestamp2)]
phase1 = phase1[:len(phase2)]

plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'

fig, ax = plt.subplots(figsize=(6, 4.5))

ax.set_ylim(-0.05, 0.9)
# ax.set_yscale('log')
# ticks = (0, 1, 2, 3, 4, 5, 6, 7)
ticks = (0, 5, 10, 15, 20, 25, 30, 35)
ax.set_yticks(ticks)

scale = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
# tickLabels = ['0', '1', '2', '3', '4', '5', '6', '7']
tickLabels = ['0', '5', '10', '15', '20', '25', '30', '35']
ax.set_xticklabels(scale, fontproperties='Times New Roman', fontsize=20, fontweight='bold')
ax.set_yticklabels(tickLabels, fontproperties='Times New Roman', fontsize=20, fontweight='bold')

# ax.set_yticklabels(tickLabels, fontproperties='Times New Roman', fontsize=14, fontweight='bold')
ax.set_xlabel('时间戳', fontsize=20)
ax.set_ylabel('相位（rad）', fontsize=20)
# ax.set_xlabel('标签方向', fontproperties='Times New Roman', fontsize=24, fontweight='bold')
# ax.set_ylabel('相位（rad）', fontproperties='Times New Roman', fontsize=24, fontweight='bold')
plt.grid(axis="y", linestyle='--', linewidth=0.8, color='#e1e2e3', zorder=0)

ax.scatter(x=timestamp1, y=phase1, alpha=0.4, s=0.6, label="距离1")
ax.scatter(x=timestamp2, y=phase2, alpha=0.4, s=0.6, c='red', label="距离2")

plt.legend()
# foo_fig = plt.gcf()  # 'get current figure'
# foo_fig.savefig(f'D:/Graduate/Paper Writing/大论文/Figure/解卷绕.pdf', format='pdf',
#                 dpi=400, bbox_inches='tight')
# foo_fig.savefig(f'D:/Graduate/Paper Writing/大论文/Figure/3_不同距离下同一标签的相位变化.png', format='png',
#                 dpi=400, bbox_inches='tight')

plt.show()
