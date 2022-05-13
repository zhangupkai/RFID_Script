import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import MultipleLocator, FixedLocator

# bath_dir = 'D:/Coding/RFID/RFID_Script/DataProcess/' \
#            'auto_rotation/phase_time_sequence/final_experiment/2_rotation_level/level_2/C001_C002(1).csv'
bath_dir = 'D:/Coding/RFID/RFID_Script/DataProcess/' \
           'auto_rotation/phase_time_sequence/final_experiment/2_rotation_level/level_2/C003_C004(2).csv'
# bath_dir = 'D:/Coding/RFID/RFID_Script/DataProcess/' \
#            'auto_rotation/phase_time_sequence/final_experiment/2_rotation_level/level_2/F002_F003(1).csv'

tag_pair_type = 2

data = np.array(pd.read_csv(bath_dir, header=None))
timestamp = data[:, 0]
phase = data[:, 1]

plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'

fig, ax = plt.subplots(figsize=(6, 4.5))

ax.set_ylim(-0.05, 0.9)
# ax.set_yscale('log')
ticks = (0, 0.2, 0.4, 0.6, 0.8)
ax.set_yticks(ticks)

scale = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
tickLabels = ['0', '0.2', '0.4', '0.6', '0.8']
ax.set_xticklabels(scale, fontproperties='Times New Roman', fontsize=20, fontweight='bold')
ax.set_yticklabels(tickLabels, fontproperties='Times New Roman', fontsize=20, fontweight='bold')

# ax.set_yticklabels(tickLabels, fontproperties='Times New Roman', fontsize=14, fontweight='bold')
ax.set_xlabel('Timestamp', fontproperties='Times New Roman', fontsize=24, fontweight='bold')
ax.set_ylabel('Phase Diff', fontproperties='Times New Roman', fontsize=24, fontweight='bold')
plt.grid(axis="y", linestyle='--', linewidth=0.8, color='#e1e2e3', zorder=0)

ax.scatter(x=timestamp, y=phase, alpha=0.4, s=0.6)
foo_fig = plt.gcf()  # 'get current figure'
foo_fig.savefig(f'D:/Graduate/Paper Writing/matlab/my_code/fig/phase_time_tag_pair_{tag_pair_type}.pdf', format='pdf',
                dpi=1000, bbox_inches='tight')
foo_fig.savefig(f'D:/Graduate/Paper Writing/matlab/my_code/fig/phase_time_tag_pair_{tag_pair_type}.png', format='png',
                dpi=1000, bbox_inches='tight')

plt.show()
