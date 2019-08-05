#encoding=utf-8

# 2001.py:计算用户最喜欢的商品的类型
import pandas as pd
# 使用更新的0626数据
# 列了两种求mode众数的方法 前者效率更高
train_path = '/home/kesci/input/data_AE3941/Antai_AE_round1_train_20190626/Antai_AE_round1_train_20190626.csv'
attri_path = '/home/kesci/input/data_AE3941/Antai_AE_round1_item_attr_20190626.csv'
# test_path =  '../../data/0626/Antai_AE_round1_test_20190626.csv'
train = pd.read_csv(train_path, encoding='utf-8')
attr_ = pd.read_csv(attri_path, encoding='utf-8')
all_buy_record = pd.merge(train[['buyer_admin_id','item_id']],attr_[['item_id','cate_id']],on='item_id',how='left')
# print all_buy_record['buyer_admin_id'].nunique()
all_buy_record = all_buy_record.dropna()
# 问 ：为什么会导致减少？ 809189   809213
# 答：因为有些cate_id为NaN
# print all_buy_record['buyer_admin_id'].nunique()

t = all_buy_record.groupby('buyer_admin_id')['cate_id'].apply(pd.Series.mode)  
t.to_csv("/home/kesci/work/1012.csv")    # 结果1：众数情况 用于下面处理
# print t.describe()

# 读取用户最喜欢的商品类型表
# 提取策略：
# 1.将那些只有一个众数的用户提取出来
# 2.把有众多众数的用户的favorite设为最后一个购买商品的类型
buyer_fav_cate = pd.read_csv("/home/kesci/work/1012.csv", encoding='utf-8')  # 使用结果1
buyer_fav_cate.columns = ['buyer_admin_id',"x",'cate_id']
buyer_fav_cate_single = pd.DataFrame(buyer_fav_cate.groupby('buyer_admin_id')['x'].count())
buyer_fav_cate_single.columns = ['type_count']

buyer_fav_cate_single_ = buyer_fav_cate_single[buyer_fav_cate_single.type_count==1] # 第一类
to_be_set_ = buyer_fav_cate_single[buyer_fav_cate_single.type_count!=1]   # 第二类

buyer_fav_cate_single_ = buyer_fav_cate_single_.reset_index()
#-----
#train_df的表需要处理，保留最后一个datetime
train_df = pd.read_csv(train_path, encoding='utf-8')
train_df = train_df.sort_values(['buyer_admin_id','create_order_time'])
train_df_last_single = train_df.drop_duplicates('buyer_admin_id',keep='last') #结果2：单众数用户的最后一次购买记录
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
attri_df = pd.read_csv(attri_path, encoding='utf-8')
merge_many_mode = pd.merge(merge_many_mode,attri_df,on='item_id',how='left')# 结果3：多众数用户的购买记录左并属性表
del merge_many_mode['item_id'],merge_many_mode['store_id'],merge_many_mode['item_price']# 删去多余特征
# 3.整合以上两个结果，由此得到所有用户的fav_cate
# 问： 这里为什么有数据的减少1？
# print len(merge_single_mode) #618143
# print len(merge_many_mode) #191045
result = merge_single_mode.append(merge_many_mode)
# print len(result)   # 809188
result.columns = ['buyer_admin_id','fav_cate']
result.to_csv("/home/kesci/work/2001.py")
# print result.describe()
