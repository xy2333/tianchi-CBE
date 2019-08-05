#encoding=utf-8
# 读取用户最喜欢的商品类型表
# 提取策略：
# 1.将那些只有一个众数的用户提取出来
# 2.把有众多众数的用户的favorite设为最后一个购买商品的类型
import pandas as pd
train_path = "../../data/0626/Antai_AE_round1_train_20190626.csv"
train_df = pd.read_csv(train_path, encoding='utf-8')
buyer_fav_cate_path = '../../result/1012.csv'
buyer_fav_cate = pd.read_csv(buyer_fav_cate_path, encoding='utf-8')
buyer_fav_cate.columns = ['buyer_admin_id',"x",'cate_id']
# single = buyer_fav_cate[buyer_fav_cate.x==0]
# print single.describe()
buyer_fav_cate_single = pd.DataFrame(buyer_fav_cate.groupby('buyer_admin_id')['x'].count())
buyer_fav_cate_single.columns = ['type_count']

buyer_fav_cate_single_ = buyer_fav_cate_single[buyer_fav_cate_single.type_count==1] # 第一类
to_be_set_ = buyer_fav_cate_single[buyer_fav_cate_single.type_count!=1]   # 第二类

buyer_fav_cate_single_ = buyer_fav_cate_single_.reset_index()
#-----
#train_df的表需要处理，保留最后一个datetime
train_path = "../../data/0626/Antai_AE_round1_train_20190626.csv"
train_df = pd.read_csv(train_path, encoding='utf-8')
train_df = train_df.sort_values(['buyer_admin_id','create_order_time'])
train_df_last_single = train_df.drop_duplicates('buyer_admin_id',keep='last')
#-----
# 1.将那些只有一个众数的用户提取出来
merge_single_mode = pd.merge(buyer_fav_cate_single_,buyer_fav_cate,on='buyer_admin_id',how='left')
print len(merge_single_mode) #
del merge_single_mode['type_count'],merge_single_mode['x']
# 2.把有众多众数的用户的favorite设为最后一个购买商品的类型
to_be_set_ = to_be_set_.reset_index()
merge_many_mode = pd.merge(to_be_set_,train_df_last_single,on='buyer_admin_id',how='left')
print len(merge_many_mode) #
del merge_many_mode['type_count'],merge_many_mode['buyer_country_id'],merge_many_mode['create_order_time'],merge_many_mode['irank']
# 第二个结果是item_id，需要和attri表关联得到cate_id
attri_df = pd.read_csv('../../data/0626/Antai_AE_round1_item_attr_20190626.csv' , encoding='utf-8')
merge_many_mode = pd.merge(merge_many_mode,attri_df,on='item_id',how='left')
del merge_many_mode['item_id'],merge_many_mode['store_id'],merge_many_mode['item_price']
# 3.整合以上两个结果，由此得到所有用户的fav_cate
# 问： 这里为什么有数据的减少1？
# print len(merge_single_mode) #618143
# print len(merge_many_mode) #191045
result = merge_single_mode.append(merge_many_mode)
# print len(result)   # 809188
result.columns = ['buyer_admin_id','fav_cate']
print result.describe()
print ""