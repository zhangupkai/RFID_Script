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

bath_dir = "D:\\Documents\\WeChat Files\\wxid_155zf28k7chf12\FileStorage\\File\\2022-10" \
           "\\TwoAnteWJL-2020-01-03-1578034248228-sp0.1x0.86dis0.4.csv"

tag_pair_type = 3
tag1 = '1002'

df = pd.read_csv(bath_dir, header=None, names=['epc', 'timestamp', 'phase', 'rssi', 'unknown1', 'port', 'freq'])
df = df[df['port'] == 2]

grouped = df.groupby('epc')

data1 = np.array(grouped.get_group(tag1))

timestamp1 = data1[:, 1]
timestamp1 = timestamp1[:120]
phase1 = data1[:, 2]
phase1 = phase1[:120]
phase1 = myunwrap.unwrap(phase1)

plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'

fig, ax = plt.subplots(figsize=(6, 4.5))

# ax.set_ylim(0, 6.29)
# ax.set_yscale('log')
# ticks = (0, 1, 2, 3, 4, 5, 6, 7)
# ticks = (0, 5, 10, 15, 20, 25, 30, 35)
# ax.set_yticks(ticks)

scale = ['0', '1', '2', '3', '4', '5', '6', '7']
# tickLabels = ['0', '1', '2', '3', '4', '5', '6', '7']
tickLabels = ['-30', '-25', '-20', '-15', '-10', '-5', '0']
ax.set_xticklabels(scale, fontproperties='Times New Roman', fontsize=20, fontweight='bold')
ax.set_yticklabels(tickLabels, fontproperties='Times New Roman', fontsize=20, fontweight='bold')

# ax.set_yticklabels(tickLabels, fontproperties='Times New Roman', fontsize=14, fontweight='bold')
ax.set_xlabel('时间戳', fontsize=20)
ax.set_ylabel('相位（rad）', fontsize=20)
# ax.set_xlabel('标签方向', fontproperties='Times New Roman', fontsize=24, fontweight='bold')
# ax.set_ylabel('相位（rad）', fontproperties='Times New Roman', fontsize=24, fontweight='bold')
plt.grid(axis="y", linestyle='--', linewidth=0.8, color='#e1e2e3', zorder=0)

ax.scatter(timestamp1, phase1, alpha=1, s=15)

plt.legend()
foo_fig = plt.gcf()  # 'get current figure'
# foo_fig.savefig(f'D:/Graduate/Paper Writing/大论文/Figure/解卷绕.pdf', format='pdf',
#                 dpi=400, bbox_inches='tight')
foo_fig.savefig(f'D:/Graduate/Paper Writing/大论文/Figure/2_解卷绕相位_new.png', format='png',
                dpi=400, bbox_inches='tight')

plt.show()
