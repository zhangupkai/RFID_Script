from cal_rotation_cycle_time_B016_B023 import cal_rotation_cycle_time_B016_B023


def cal_rotation_cycle_time(timestamp, phase, tag_pair):
    # if tag_pair == 'B034_B029':
    #     return locate_degree_B034_B029(phase)
    # elif tag_pair == 'B016_AA03':
    #     return locate_degree_B016_AA03(phase)
    if tag_pair == 'B016_B023':
        return cal_rotation_cycle_time_B016_B023(timestamp, phase)
