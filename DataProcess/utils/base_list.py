# 生成功率列表
def get_power_list():
    power_list = []
    for x in range(0, 8):
        power = 24.0 + x
        power_list.append(power)
    return power_list


# 生成频率列表
def get_freq_list():
    freq_list = []
    for x in range(0, 8):
        freq = 920.625 + x * 0.5
        freq_list.append(freq)
    return freq_list
