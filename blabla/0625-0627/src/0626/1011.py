#encoding=utf-8

import pandas as pd
# 数据更新
# 计算用户最喜欢的商品的类型，最喜欢的商铺  列了两种求mode众数的方法 前者效率更高
train_path = '../../data/0626/Antai_AE_round1_train_20190626.csv'
attri_path = '../../data/0626/Antai_AE_round1_item_attr_20190626.csv'

train = pd.read_csv(train_path, encoding='utf-8')
attr_ = pd.read_csv(attri_path, encoding='utf-8')

all_buy_record = pd.merge(train[['buyer_admin_id','item_id']],attr_[['item_id','cate_id']],on='item_id',how='left')
import scipy.stats.mstats as mstats
def mode(x):
    return mstats.mode(x, axis=None)[0]
all_buy_record = all_buy_record.dropna()
# print len(all_buy_record)
# print all_buy_record.describe()
# res = all_buy_record.groupby(['buyer_admin_id','cate_id']).agg({'cate_id':mode})
t = all_buy_record.iloc[:6000000,:].groupby('buyer_admin_id')['cate_id'].apply(mode)
t.to_csv('../../result/1011_1.csv')
del t
t = all_buy_record.iloc[6000000:,:].groupby('buyer_admin_id')['cate_id'].apply(mode)
t.to_csv('../../result/1011_2.csv')
print t.describe()
