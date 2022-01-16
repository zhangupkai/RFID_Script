import numpy as np
import pandas as pd
# 导入模型
from sklearn.tree import DecisionTreeClassifier
# 数据分割包
from sklearn.model_selection import train_test_split
# 评价包
from sklearn.metrics import mean_squared_error
from sklearn.metrics import accuracy_score
# 规范化数据包
from sklearn import preprocessing


"""
将每个标签阵列的9x8数据flatten，成为72个特征，存入到训练数据中
"""
if __name__ == '__main__':
    print(0)
    sava_path = 'train_data/B016_B023.csv'
    data = np.array(pd.read_csv('../../tagPair/data/distance_50cm/B016_B023/B016_B023(1).csv', header=None))
    flatten_data = data.flatten()
