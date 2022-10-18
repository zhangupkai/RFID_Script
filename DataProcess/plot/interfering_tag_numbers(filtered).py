import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator, FixedLocator

condition = 'interfering_tag_numbers(filtered)'
x_label = '环境中干扰标签的数量'
y_label = '准确率'
scale = ['0', '30', '40', '60']
database = ['Legitimate', 'Illegitimate']
colorOfColum = ['#90C9E7', '#136783']
size = ['//', '']
# colorOfColum = ['#B44DE0', '#4DBB9D', '#89CBF0', 'grey', '#EEBC4D']
data = (
    (0.9882, 0.9926),
    (0.9444, 0.9600),
    (0.9227, 0.9414),
    (0.9271, 0.9460),
)

dim = len(data[0])
total_width = 1
width = total_width / (dim + 1)
columnWidth = total_width / (dim + 2)
experiment_num = len(data)

plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'

fig, ax = plt.subplots(figsize=(9, 6.75))
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
# 所有的柱右移一个width距离，避免和坐标轴重叠
x = np.arange(experiment_num) + width
for i in range(dim):
    y = [d[i] for d in data]
    ax.bar(x + width * i, y, columnWidth, bottom=0, label=database[i], color=colorOfColum[i], linewidth=0.8,
           edgecolor='black', zorder=2, hatch=size[i])

legend_properties = {'family': 'Times New Roman', 'weight': 'bold', 'size': 30}
ax.legend(prop=legend_properties, shadow=False, framealpha=1, ncol=1, loc='lower right', facecolor='white',
          edgecolor='black')

ax.set_xlim(0, total_width * experiment_num)
ax.xaxis.set_major_locator(FixedLocator([0.5 + i for i in range(len(data))]))
ax.set_xticklabels(scale, fontproperties='Times New Roman', fontsize=30, fontweight='bold')
ax.xaxis.set_minor_locator(MultipleLocator(total_width))

ax.set_ylim(0, 1)
# ax.set_yscale('log')
ticks = (0, 0.2, 0.4, 0.6, 0.8, 1)
ax.set_yticks(ticks)
# ax.grid(True)
tickLabels = ['0', '0.2', '0.4', '0.6', '0.8', '1']
ax.set_yticklabels(tickLabels, fontproperties='Times New Roman', fontsize=30, fontweight='bold')
ax.set_xlabel(x_label, fontproperties='SimSun', fontsize=30, fontweight='bold', labelpad=8.5)
ax.set_ylabel(y_label, fontproperties='SimSun', fontsize=30, fontweight='bold', labelpad=8.5)
plt.grid(axis="y", linestyle='--', linewidth=0.8, color='#e1e2e3', zorder=0)

ax.spines['bottom'].set_linewidth(0.8)
ax.spines['left'].set_linewidth(0.8)
ax.spines['right'].set_linewidth(0.8)
ax.spines['top'].set_linewidth(0.8)

ax.tick_params(axis='y', length=5, width=0.8)
ax.tick_params(axis='x', which='minor', length=0, width=0.8)
ax.tick_params(axis='x', which='major', length=0, width=0.8)

foo_fig = plt.gcf()  # 'get current figure'
# foo_fig.savefig('distance.pdf', format='pdf', dpi=1000)
# foo_fig.savefig(f'D:/Graduate/Paper Writing/matlab/my_code/fig/{condition}.eps', format='eps', dpi=1000,
#                 bbox_inches='tight')
foo_fig.savefig(f'D:/Graduate/Paper Writing/大论文/Figure/3_干扰标签数量的影响.png', format='png', dpi=400,
                bbox_inches='tight')
plt.show()

