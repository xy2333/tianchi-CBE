#encoding=utf-8

# 2002.py:计算用户最喜欢的店铺 
# 提取策略：
# 1.将那些只有一个众数的用户提取出来
# 2.把有众多众数的用户的favorite设为最后一个购买商品的店铺
#encoding=utf-8

import pandas as pd
# 计算用户最喜欢的商铺
train_path = '/home/kesci/input/data_AE3941/Antai_AE_round1_train_20190626/Antai_AE_round1_train_20190626.csv'
attri_path = '/home/kesci/input/data_AE3941/Antai_AE_round1_item_attr_20190626.csv'

train = pd.read_csv(train_path, encoding='utf-8')
attr_ = pd.read_csv(attri_path, encoding='utf-8')

all_buy_record = pd.merge(train[['buyer_admin_id','item_id']],attr_[['item_id','store_id']],on='item_id',how='left')
del train,attr_
# print len(all_buy_record)12868509

all_buy_record = all_buy_record.dropna()
# print len(all_buy_record)12843064 直接使用dropna后的数据 
buyer_fav_store = pd.DataFrame(all_buy_record.groupby('buyer_admin_id')['store_id'].apply(pd.Series.mode))
buyer_fav_store = buyer_fav_store.reset_index()
buyer_fav_store.columns = ['buyer_admin_id',"x",'store_id']

# 提取策略：
# 1.将那些只有一个众数的用户提取出来
# 2.把有众多众数的用户的favorite设为最后一个购买商品的店铺

buyer_fav_store_single = pd.DataFrame(buyer_fav_store.groupby('buyer_admin_id')['x'].count()) #error:keyerror :buyer_admin_id
buyer_fav_store_single.columns = ['sotre_count']

buyer_fav_store_single_ = buyer_fav_store_single[buyer_fav_store_single.sotre_count==1] # 第一类
to_be_set_ = buyer_fav_store_single[buyer_fav_store_single.sotre_count!=1]   # 第二类

buyer_fav_store_single_ = buyer_fav_store_single_.reset_index()
#-----
#train_df的表需要处理，保留最后一个datetime
train = pd.read_csv(train_path, encoding='utf-8') # 前面del去了，现在重新加载
train_df_sorted = train.sort_values(['buyer_admin_id','create_order_time'])
del train
train_df_last_single = train_df_sorted.drop_duplicates('buyer_admin_id',keep='last')
#-----
# 1.将那些只有一个众数的用户提取出来
merge_single_mode = pd.merge(buyer_fav_store_single_,buyer_fav_store,on='buyer_admin_id',how='left')
# print len(merge_single_mode) #504035
del merge_single_mode['sotre_count'],merge_single_mode['x']
# 2.把有众多众数的用户的favorite设为最后一个购买商品的类型
to_be_set_ = to_be_set_.reset_index()
merge_many_mode = pd.merge(to_be_set_,train_df_last_single,on='buyer_admin_id',how='left')
# print len(merge_many_mode) #161270     += 665305
del train_df_last_single,merge_many_mode['sotre_count'],merge_many_mode['buyer_country_id'],merge_many_mode['create_order_time']#,merge_many_mode['irank']
# 第二个结果是item_id，需要和attri表关联得到cate_id
attri_df = pd.read_csv('/home/kesci/input/data_AE3941/Antai_AE_round1_item_attr_20190626.csv' , encoding='utf-8')
merge_many_mode = pd.merge(merge_many_mode,attri_df,on='item_id',how='left')
del merge_many_mode['item_id'],merge_many_mode['item_price'],merge_many_mode['irank'],merge_many_mode['cate_id']
# print merge_single_mode.info()
# print merge_many_mode.info()
# 3.整合以上两个结果，由此得到所有用户的fav_cate

result = merge_single_mode.append(merge_many_mode)
result.columns = ['buyer_admin_id','fav_store']
result.to_csv("/home/kesci/work/2002.csv")  # 665174
# print result.describe()
# print ""

