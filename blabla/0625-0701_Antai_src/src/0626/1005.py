#encoding=utf-8

import pandas as pd
# 计算用户最喜欢的商品的类型，最喜欢的商铺
train_path = '../../data/Antai_AE_round1_train_20190625.csv'
attri_path = '../../data/[new] Antai_AE_round1_item_attr_20190625.csv'
test_path =  '../../data/Antai_AE_round1_test_20190625.csv'
train = pd.read_csv(train_path, encoding='utf-8')
attr_ = pd.read_csv(attri_path, encoding='utf-8')

# 计算用户最喜欢的商品的类型 #store_id item_price
all_buy_record = pd.merge(train[['buyer_admin_id','item_id']],attr_[['item_id','cate_id']],on='item_id',how='left')
# t = all_buy_record.iloc[:200,:].sort_values('buyer_admin_id')
# 以下可以求出众数
# temp = all_buy_record.iloc[:200,:].groupby(['buyer_admin_id','cate_id']).apply(pd.DataFrame.mode).reset_index(drop=True)
# print temp.describe()# item_id 有10 012 800 条; cate_id 有 9 966 641(不是unique,有7M多条NaN)
result = all_buy_record.groupby(['buyer_admin_id','cate_id']).apply(pd.DataFrame.mode).reset_index(drop=True)
result.to_csv("../../result/1005.csv")
print ""
