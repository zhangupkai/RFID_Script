import numpy as np
import copy


# 归一化
def normalization(input_data):
    _range = np.max(input_data) - np.min(input_data)
    return (input_data - np.min(input_data)) / _range


# 处理相位序列中零值
def deal_zero_phase(input_phase):
    if input_phase[0] == 0:
        input_phase[0] = np.min(input_phase[np.nonzero(input_phase)])
    for index in range(1, 8):
        if input_phase[index] == 0:
            input_phase[index] = input_phase[index - 1]
    return input_phase


# f1~f8的相位是否发生了跳变
def is_phase_hop(input_phase):
    max_phase = np.max(input_phase)
    min_phase = np.min(input_phase)
    if max_phase - min_phase > 5:
        return True
    else:
        return False
