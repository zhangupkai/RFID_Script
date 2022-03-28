from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

filepath = 'dataset_group2'
data = pd.read_csv(f'{filepath}/dataset.csv', header=None)
messages = data.iloc[:, 0]
y = data.iloc[:, 1]

messages_train, messages_test, y_train, y_test = train_test_split(messages, y, test_size=0.3, random_state=1000)

train = np.column_stack((messages_train, y_train))
test = np.column_stack((messages_test, y_test))

train_data = f'{filepath}/trainDataInfo.csv'
test_data = f'{filepath}/testDataInfo.csv'
pd.DataFrame(train).to_csv(train_data, index=False, header=False)
pd.DataFrame(test).to_csv(test_data, index=False, header=False)

# 加载数据，查看条数
df_train = pd.read_csv(train_data, sep=',', encoding='utf-8')
df_test = pd.read_csv(test_data, sep=',', encoding='utf-8')
print('训练集大小', len(df_train), '测试集大小', len(df_test))
