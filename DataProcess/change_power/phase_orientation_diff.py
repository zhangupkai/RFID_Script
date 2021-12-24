import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import copy

if __name__ == '__main__':
    distance = '50cm'
    bath_dir = 'data/set_four_orientation/distance_' + distance + '/'
    data = np.array(pd.read_csv(bath_dir + 'B016_B023_B023(2).csv', header=None))

    diff_B016_B023 = data[0, ] - data[2, ]
    diff_B023_2_B023 = data[2, ] - data[1, ]

    x = [0, 45, 90, 135, 180, 225, 270, 315, 360]
    plt.plot(x, diff_B016_B023, 's-', color='black', label='diff_B016_B023')
    plt.plot(x, diff_B023_2_B023, 's-', color='red', label='diff_B023(2)_B023')

    plt.title("Distance " + distance)
    plt.xlabel("Orientation")
    plt.ylabel("Phase Diff")
    plt.legend()
    plt.show()
