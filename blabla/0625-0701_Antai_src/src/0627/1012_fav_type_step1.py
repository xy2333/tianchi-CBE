#encoding=utf-8

import pandas as pd
# 数据更新
# 计算用户最喜欢的商品的类型，最喜欢的商铺  列了两种求mode众数的方法 前者效率更高
train_path = '../../data/0626/Antai_AE_round1_train_20190626.csv'
attri_path = '../../data/0626/Antai_AE_round1_item_attr_20190626.csv'
# test_path =  '../../data/0626/Antai_AE_round1_test_20190626.csv'
train = pd.read_csv(train_path, encoding='utf-8')
attr_ = pd.read_csv(attri_path, encoding='utf-8')

all_buy_record = pd.merge(train[['buyer_admin_id','item_id']],attr_[['item_id','cate_id']],on='item_id',how='left')
# print all_buy_record['buyer_admin_id'].nunique()
all_buy_record = all_buy_record.dropna()
# 问 ：为什么会导致减少？ 809189   809213
# 答：因为有些cate_id为NaN
print all_buy_record['buyer_admin_id'].nunique()
all_buy_record.to_csv('../../result/1012_train_merge_atti_dropna.csv')
t = all_buy_record.groupby('buyer_admin_id')['cate_id'].apply(pd.Series.mode)
t.to_csv("../../result/1012.csv")
print t.describe()