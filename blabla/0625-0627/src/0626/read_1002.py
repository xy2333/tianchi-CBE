#encoding=utf-8
import pandas as pd
import time
train_path = '../../result/1002.csv'
train = pd.read_csv(train_path, encoding='utf-8')
print train.describe()
print ""