import numpy as np


# 归一化
def normalization(input_data):
    _range = np.max(input_data) - np.min(input_data)
    return (input_data - np.min(input_data)) / _range


"""

"""


# f1~f8的相位是否发生了跳变
def is_phase_hop(input_phase):
    max_phase = np.max(input_phase)
    min_phase = np.min(input_phase)
    if max_phase - min_phase > 5:
        return True
    else:
        return False
