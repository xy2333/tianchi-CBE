#encoding=utf-8
# 读取用户最喜欢的店铺 (未开始做）
# 提取策略：
# 1.将那些只有一个众数的用户提取出来
# 2.把有众多众数的用户的favorite设为最后一个购买商品的店铺
#encoding=utf-8

import pandas as pd
# 计算用户最喜欢的商铺
train_path = '../../data/0626/Antai_AE_round1_train_20190626.csv'
attri_path = '../../data/0626/Antai_AE_round1_item_attr_20190626.csv'
# test_path =  '../../data/0626/Antai_AE_round1_test_20190626.csv'
train = pd.read_csv(train_path, encoding='utf-8')
attr_ = pd.read_csv(attri_path, encoding='utf-8')

all_buy_record = pd.merge(train[['buyer_admin_id','item_id']],attr_[['item_id','store_id']],on='item_id',how='left')
del train,attr_
all_buy_record = all_buy_record.dropna()
t = all_buy_record.groupby('buyer_admin_id')['store_id'].apply(pd.Series.mode)
t.to_csv("../../result/1017.csv")
print t.describe()