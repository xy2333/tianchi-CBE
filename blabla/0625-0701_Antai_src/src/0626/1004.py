#encoding=utf-8

# 将train表的四个is_morning,afternoon,night,midnight进一步处理 得到其比例

import pandas as pd
import time
train_path = '../../result/1002.csv'
train = pd.read_csv(train_path, encoding='utf-8')

# t2 = train[train.buyer_admin_id=='3157']
# t3 = train[train.buyer_admin_id==3157]//

night_times = train.groupby('buyer_admin_id')['is_night'].sum()  # 1 0 0 1 对应2
night_all_times = train.groupby('buyer_admin_id')['is_night'].count() # 1 0 0 1 对应4
night_percen = night_times/night_all_times
# 2/4 即得到在夜晚购物的比例
morning_times = train.groupby('buyer_admin_id')['is_morning'].sum()
morning_all_times = train.groupby('buyer_admin_id')['is_morning'].count()
morning_percen = morning_times/morning_all_times

afternoon_times = train.groupby('buyer_admin_id')['is_afternoon'].sum()
afternoon_all_times = train.groupby('buyer_admin_id')['is_afternoon'].count()
afternoon_percen = afternoon_times/afternoon_all_times

midnight_times = train.groupby('buyer_admin_id')['is_midnight'].sum()
midnight_all_times = train.groupby('buyer_admin_id')['is_midnight'].count()
midnight_percen = midnight_times/midnight_all_times

morning_percen = morning_percen.reset_index()
afternoon_percen = afternoon_percen.reset_index(drop=True)
night_percen = night_percen.reset_index(drop=True)
midnight_percen = midnight_percen.reset_index(drop=True)

result = morning_percen.join(afternoon_percen).join(night_percen).join(midnight_percen)
print ""
