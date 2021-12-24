import numpy as np


# 归一化
def normalization(input_data):
    _range = np.max(input_data) - np.min(input_data)
    return (input_data - np.min(input_data)) / _range