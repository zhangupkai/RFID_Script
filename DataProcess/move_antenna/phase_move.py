import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from myunwrap import unwrap
from filters import hampel
from pre_purpose import normalization


if __name__ == '__main__':
    bath_dir = '../../data/moveAntenna/'
    degree = 'degree_0'
    count = '(1)'
    colors = ['red', 'blue', 'green', 'yellow']
    file_path = bath_dir + degree + '/B023' + count + '.csv'

    df = pd.read_csv(file_path, header=None, names=['epc', 'freq', 'timestamp', 'phase', 'rssi'])
    # 时间戳归一化
    df['timestamp'] = normalization(df['timestamp'])
    # 相位unwrap
    df['phase'] = unwrap(df['phase'])
    grouped = df.groupby('freq')

    i = 0
    for name, group in grouped:
        plt.scatter(group['timestamp'], group['phase'], c=colors[i], alpha=0.6)
        save_path = bath_dir + 'phase_time_sequence'
        group.to_csv()
        i += 1

    plt.show()
