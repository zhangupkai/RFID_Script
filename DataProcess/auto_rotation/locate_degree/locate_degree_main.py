import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from locate_degree_detail import *


def locate_degree(timestamp, phase, tag_pair, freq):
    if tag_pair == 'B034_B029':
        return locate_degree_B034_B029(phase)
    elif tag_pair == 'B016_AA03':
        return locate_degree_B016_AA03(phase)
    elif tag_pair == 'B016_B023':
        return locate_degree_B016_B023(phase)
    elif tag_pair == 'E002_C001':
        return locate_degree_E002_C001(phase, freq)
    elif tag_pair == 'E002_E006' or tag_pair == 'E004_E005':
        return locate_degree_E002_E006(phase, freq)
    elif tag_pair == 'F001_F005':
        return locate_degree_F001_F005(phase, freq)
    elif tag_pair == 'F001_E006':
        return locate_degree_F001_E006(phase, freq)
    elif tag_pair == 'C001_C002':
        return locate_degree_C001_C002(phase, freq)
