import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from locate_degree_B034_B029 import locate_degree_B034_B029
from locate_degree_B016_AA03 import locate_degree_B016_AA03


def locate_degree(phase, tag_pair):
    if tag_pair == 'B034_B029':
        return locate_degree_B034_B029(phase)
    elif tag_pair == 'B016_AA03':
        return locate_degree_B016_AA03(phase)
