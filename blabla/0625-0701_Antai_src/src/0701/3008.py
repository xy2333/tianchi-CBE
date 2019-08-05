# 3008.py:计算用户最喜欢的店铺 数据来自3006：已去除最后一条记录

# 1.将那些只有一个众数的用户提取出来
# 2.把有众多众数的用户的favorite设为最后一个购买商品的店铺

import pandas as pd
# 计算用户最喜欢的商铺
train_path = "/home/kesci/work/3006_xx_train_X.csv"
attri_path = '/home/kesci/input/data_AE3941/Antai_AE_round1_item_attr_20190626.csv'

df = pd.read_csv(train_path, encoding='utf-8')
attr_ = pd.read_csv('/home/kesci/input/data_AE3941/Antai_AE_round1_item_attr_20190626.csv', encoding='utf-8')
all_buy_record = pd.merge(df[['buyer_admin_id','item_id']],attr_[['item_id','store_id']],on='item_id',how='left').dropna()
del df,attr_
buyer_fav_store = pd.DataFrame(all_buy_record.groupby('buyer_admin_id')['store_id'].apply(pd.Series.mode))
buyer_fav_store = buyer_fav_store.reset_index()
buyer_fav_store.columns = ['buyer_admin_id',"x",'store_id']

# 计算出只有一个众数的和有若干个总数的
buyer_fav_store_single = pd.DataFrame(buyer_fav_store.groupby('buyer_admin_id')['x'].count()) 
buyer_fav_store_single.columns = ['sotre_count']
# 第一类：将那些只有一个众数的用户提取出来
# 第二类：把有众多众数的用户的favorite设为最后一个购买商品的店铺
buyer_fav_store_single_ = buyer_fav_store_single[buyer_fav_store_single.sotre_count==1] # 第一类
to_be_set_ = buyer_fav_store_single[buyer_fav_store_single.sotre_count!=1]   # 第二类

# 计算第一类
buyer_fav_store_single_ = buyer_fav_store_single_.reset_index()
merge_single_mode = pd.merge(buyer_fav_store_single_,buyer_fav_store,on='buyer_admin_id',how='left')
del merge_single_mode['sotre_count'],merge_single_mode['x']

# 计算第二类
# 得到测试集中每个用户最后一条记录
test_df_last_single = pd.read_csv(train_path, encoding='utf-8').sort_values(['buyer_admin_id','create_order_time']).drop_duplicates('buyer_admin_id',keep='last')
to_be_set_ = to_be_set_.reset_index()
# 和上面结果关联
merge_many_mode = pd.merge(to_be_set_,test_df_last_single,on='buyer_admin_id',how='left')
del test_df_last_single,merge_many_mode['sotre_count'],merge_many_mode['buyer_country_id'],merge_many_mode['create_order_time']#,merge_many_mode['irank']
# 和attri表关联得到cate_id
attri_df = pd.read_csv('/home/kesci/input/data_AE3941/Antai_AE_round1_item_attr_20190626.csv' , encoding='utf-8')
merge_many_mode = pd.merge(merge_many_mode,attri_df,on='item_id',how='left')
del merge_many_mode['item_id'],merge_many_mode['item_price'],merge_many_mode['irank'],merge_many_mode['cate_id']
# 3.整合以上两个结果，由此得到所有用户的fav_cate
result = merge_single_mode.append(merge_many_mode)
del result['Unnamed: 0']
result.columns = ['buyer_admin_id','fav_store']
result.to_csv("/home/kesci/work/3008.csv") 