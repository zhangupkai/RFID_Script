import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from myunwrap import unwrap
from filters import hampel


def one_tag(_tag, _color):
    bath_dir = '../../data/changeOrientation/distance_17cm/level_3/'
    file_path = bath_dir + tag + '_24.0_924.375.csv'
    data = np.array(pd.read_csv(file_path, header=None))
    phase_list = data[:, 3]
    unwrap_phase_list = unwrap(phase_list)
    plt.plot(phase_list, marker='o', markersize=3, color=_color, label=tag)


if __name__ == '__main__':
    # tags = ['B016(2)', 'B023(2)', 'A102(2)', 'C008(1)']
    # colors = ['red', 'blue', 'black', 'cyan']
    tags = ['C008(1)']
    colors = ['cyan']

    i = 0
    for tag in tags:
        one_tag(tag, colors[i])
        i += 1

    plt.title('Phase Orientation')
    plt.xlabel("Orientation")
    plt.ylabel("Phase")
    plt.legend()
    plt.show()
