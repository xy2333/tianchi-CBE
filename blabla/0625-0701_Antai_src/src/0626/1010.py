#encoding=utf-8

import pandas as pd
# 数据更新
# 计算用户最喜欢的商品的类型，最喜欢的商铺  列了两种求mode众数的方法 前者效率更高
train_path = '../../data/0626/Antai_AE_round1_train_20190626.csv'
attri_path = '../../data/0626/Antai_AE_round1_item_attr_20190626.csv'
# test_path =  '../../data/0626/Antai_AE_round1_test_20190626.csv'
train = pd.read_csv(train_path, encoding='utf-8')
attr_ = pd.read_csv(attri_path, encoding='utf-8')

# 计算用户最喜欢的商品的类型 #store_id item_price
all_buy_record = pd.merge(train[['buyer_admin_id','item_id']],attr_[['item_id','cate_id']],on='item_id',how='left')
# 以下可以求出众数
# temp = all_buy_record.iloc[:200,:].groupby(['buyer_admin_id','cate_id']).apply(pd.DataFrame.mode).reset_index(drop=True)
# print temp.describe()# item_id 有10 012 800 条; cate_id 有 9 966 641(不是unique,有7M多条NaN)
# result = all_buy_record.groupby(['buyer_admin_id','cate_id']).apply(pd.DataFrame.mode).reset_index(drop=True)
# result.to_csv("../../result/1005.csv")
# print ""

# 1.
import datetime
print(datetime.datetime.now())
r_5000 = all_buy_record.iloc[:50000,:]
import scipy.stats.mstats as mstats
def mode(x):
    return mstats.mode(x, axis=None)[0]
t = r_5000.groupby(['buyer_admin_id','cate_id']).agg({'cate_id':mode})
print(datetime.datetime.now())

# 2.
r_5000 = all_buy_record.iloc[:50000,:]
result = r_5000.groupby(['buyer_admin_id','cate_id']).apply(pd.DataFrame.mode).reset_index(drop=True)
print(datetime.datetime.now())
