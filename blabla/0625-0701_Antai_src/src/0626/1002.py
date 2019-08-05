#encoding=utf-8
import pandas as pd
import time
train_path = '../../data/Antai_AE_round1_train_20190625.csv'
train = pd.read_csv(train_path, encoding='utf-8')
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
is_morning_boo_series = train['create_order_time'].apply(lambda x: is_morning(time.strptime(str(x),"%Y-%m-%d %H:%M:%S")))
to_join = pd.DataFrame(is_morning_boo_series) # series to dataframe
to_join.columns = ['is_morning']
to_join = to_join.reset_index(drop=True)
result = train.join(to_join)
del is_morning_boo_series,to_join

is_afternoon_boo_series = train['create_order_time'].apply(lambda x: is_afternoon(time.strptime(str(x),"%Y-%m-%d %H:%M:%S")))
to_join = pd.DataFrame(is_afternoon_boo_series) # series to dataframe
to_join.columns = ['is_afternoon']
to_join = to_join.reset_index(drop=True)
result = result.join(to_join)
del is_afternoon_boo_series,to_join

is_night_boo_series = train['create_order_time'].apply(lambda x: is_night(time.strptime(str(x),"%Y-%m-%d %H:%M:%S")))
to_join = pd.DataFrame(is_night_boo_series) # series to dataframe
to_join.columns = ['is_night']
to_join = to_join.reset_index(drop=True)
result = result.join(to_join)
del is_night_boo_series,to_join

is_mid_boo_series = train['create_order_time'].apply(lambda x: is_midnight(time.strptime(str(x),"%Y-%m-%d %H:%M:%S")))
to_join = pd.DataFrame(is_mid_boo_series) # series to dataframe
to_join.columns = ['is_midnight']
to_join = to_join.reset_index(drop=True)
result = result.join(to_join)
del is_mid_boo_series,to_join

result.to_csv("../../result/1002.csv")
print ""