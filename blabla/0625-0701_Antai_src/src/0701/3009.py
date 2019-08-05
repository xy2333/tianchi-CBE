# 3009: 计算购物时间的占比 

import pandas as pd
import time

train_path = "/home/kesci/work/3006_xx_train_X.csv"
attri_path = '/home/kesci/input/data_AE3941/Antai_AE_round1_item_attr_20190626.csv'
df = pd.read_csv(train_path, encoding='utf-8')
def is_morning(dt): # 5:00-11:00  5,6,7,8,9,10
    if 5<=dt.tm_hour and dt.tm_hour<=10:
        return 1
    else:
        return 0
def is_afternoon(dt): #11:00-17:00  11,12,13,14,15,16
    if 11<=dt.tm_hour and dt.tm_hour<=16:
        return 1
    else:
        return 0
def is_night(dt):# 17:00-23:00  17 18 19 20 21 22
    if 17<=dt.tm_hour and dt.tm_hour<=22:
        return 1
    else:
        return 0
def is_midnight(dt):# 23:00-5:00  23 0 1 2 3 4
    if dt.tm_hour<=4 or dt.tm_hour==23:
        return 1
    else:
        return 0

# 对大量数据（10M级别的） apply可以做到低内存消耗，运算时间较长
is_morning_boo_series = df['create_order_time'].apply(lambda x: is_morning(time.strptime(str(x),"%Y-%m-%d %H:%M:%S")))
to_join = pd.DataFrame(is_morning_boo_series) # series to dataframe
to_join.columns = ['is_morning']
to_join = to_join.reset_index(drop=True)
result = df.join(to_join)
del is_morning_boo_series,to_join

is_afternoon_boo_series = df['create_order_time'].apply(lambda x: is_afternoon(time.strptime(str(x),"%Y-%m-%d %H:%M:%S")))
to_join = pd.DataFrame(is_afternoon_boo_series) # series to dataframe
to_join.columns = ['is_afternoon']
to_join = to_join.reset_index(drop=True)
result = result.join(to_join)
del is_afternoon_boo_series,to_join

is_night_boo_series = df['create_order_time'].apply(lambda x: is_night(time.strptime(str(x),"%Y-%m-%d %H:%M:%S")))
to_join = pd.DataFrame(is_night_boo_series) # series to dataframe
to_join.columns = ['is_night']
to_join = to_join.reset_index(drop=True)
result = result.join(to_join)
del is_night_boo_series,to_join

is_mid_boo_series = df['create_order_time'].apply(lambda x: is_midnight(time.strptime(str(x),"%Y-%m-%d %H:%M:%S")))
to_join = pd.DataFrame(is_mid_boo_series) # series to dataframe
to_join.columns = ['is_midnight']
to_join = to_join.reset_index(drop=True)
result = result.join(to_join)   # result为结果1 其特征列为is_morning...等
del is_mid_boo_series,to_join

# 将df表的四个is_morning,afternoon,night,midnight进一步处理 得到其比例

is_each_time_df = result


night_times = is_each_time_df.groupby('buyer_admin_id')['is_night'].sum()  # 1 0 0 1 对应2
night_all_times = is_each_time_df.groupby('buyer_admin_id')['is_night'].count() # 1 0 0 1 对应4
night_percen = night_times/night_all_times
# 2/4 即得到在夜晚购物的比例
morning_times = is_each_time_df.groupby('buyer_admin_id')['is_morning'].sum()
morning_all_times = is_each_time_df.groupby('buyer_admin_id')['is_morning'].count()
morning_percen = morning_times/morning_all_times

afternoon_times = is_each_time_df.groupby('buyer_admin_id')['is_afternoon'].sum()
afternoon_all_times = is_each_time_df.groupby('buyer_admin_id')['is_afternoon'].count()
afternoon_percen = afternoon_times/afternoon_all_times

midnight_times = is_each_time_df.groupby('buyer_admin_id')['is_midnight'].sum()
midnight_all_times = is_each_time_df.groupby('buyer_admin_id')['is_midnight'].count()
midnight_percen = midnight_times/midnight_all_times

morning_percen = morning_percen.reset_index()
afternoon_percen = afternoon_percen.reset_index(drop=True)
night_percen = night_percen.reset_index(drop=True)
midnight_percen = midnight_percen.reset_index(drop=True)

result = morning_percen.join(afternoon_percen).join(night_percen).join(midnight_percen)
result.to_csv("/home/kesci/work/3009.csv")

