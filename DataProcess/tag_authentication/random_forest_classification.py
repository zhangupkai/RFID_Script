from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import pandas as pd
import numpy as np

# 训练集
train_dataset = pd.read_csv('../tagPair/data/dataset/trainDataInfo.csv')

x_train_path = train_dataset.iloc[:, 0]
x_train = []
for index, value in x_train_path.iteritems():
    x_train_data = np.array(pd.read_csv('../tagPair/phase_time_sequence/' + value))
    x_train.append(x_train_data.flatten())

y_train = np.array(train_dataset.iloc[:, 1]).tolist()

# 测试集
test_dataset = pd.read_csv('../tagPair/data/dataset/testDataInfo.csv')
x_test_path = test_dataset.iloc[:, 0]
x_test = []
for index, value in x_test_path.iteritems():
    x_test_data = np.array(pd.read_csv('../tagPair/phase_time_sequence/' + value))
    x_test.append(x_test_data.flatten())

y_test = np.array(test_dataset.iloc[:, 1]).tolist()

# 决策树
dtc = DecisionTreeClassifier()
dtc.fit(x_train, y_train)
dtc_y_predict = dtc.predict(x_test)
print('Decision Tree: ', dtc.score(x_test, y_test))
print(classification_report(y_test, dtc_y_predict, target_names=['TagPair 0', 'TagPair 1', 'TagPair 2']))

# 随机森林
rfc = RandomForestClassifier()
rfc.fit(x_train, y_train)
rfc_y_predict = rfc.predict(x_test)
print('Random Forest: ', rfc.score(x_test, y_test))
print(classification_report(y_test, rfc_y_predict, target_names=['TagPair 0', 'TagPair 1', 'TagPair 2']))
