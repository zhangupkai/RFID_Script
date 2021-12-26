import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from myunwrap import unwrap
from filters import hampel
from pre_purpose import normalization
import seaborn as sns
from base_list import *

if __name__ == '__main__':
    distance = '50cm'
    tag_pair = 'B016_B023'
    tag1 = 'B016'
    tag2 = 'B023'
    count = '(2)'
    bath_dir = 'data/distance_' + distance + '/' + tag_pair + '/'
    degrees = ['degree_0', 'degree_45', 'degree_90', 'degree_135', 'degree_180',
               'degree_225', 'degree_270', 'degree_315', 'degree_360']
    sava_path = 'data/distance_' + distance + '/' + tag_pair + '/' + tag_pair + '.csv'
    phase_freq_degree = np.zeros((9, 8))

    file_path1 = bath_dir + tag1 + count + '.csv'
    file_path2 = bath_dir + tag2 + count + '.csv'
    data1 = pd.read_csv(file_path1, header=None)
    data2 = pd.read_csv(file_path2, header=None)

    phase_diff = np.abs(data1 - data2)

    sns.heatmap(phase_diff, cmap='Blues', xticklabels=get_freq_list(), yticklabels=get_degree_list())
    plt.title('Phase Diff ' + distance + ' ' + tag_pair + " " + count)
    plt.xlabel("Freq")
    plt.ylabel("Degree")
    plt.show()

    np.savetxt(sava_path, phase_diff, delimiter=',')
