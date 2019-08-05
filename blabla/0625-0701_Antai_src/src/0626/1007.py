#encoding=utf-8

# 0626 数据更新 重新分析
import pandas as pd

train_path = '../../data/0626/Antai_AE_round1_train_20190626.csv'
attri_path = '../../data/0626/Antai_AE_round1_item_attr_20190626.csv'
test_path = '../../data/0626/Antai_AE_round1_test_20190626.csv'
# item_id,cate_id,store_id,item_price

# attr表分析
attr_ = pd.read_csv(attri_path, encoding='utf-8')
# print len(attr_)    # 2416318                2832669
# print attr_['item_id'].nunique() # 2416318    2832669
# print attr_['cate_id'].nunique() # 4119       4243
# print attr_['store_id'].nunique() # 90783     95105
# print attr_['item_price'].nunique()  # 17932  20230
# print attr_.describe()
# price:
#  min:  1      1
#  25%:  176    180
#  50%:  400    400
#  75%:  1164   1200
# max:  17932   20230
# train表分析：
train = pd.read_csv(train_path, encoding='utf-8')
#
# print len(train)    # 10 012 805                         12 868 509
# print train['buyer_country_id'].nunique() # 2              2
# print train['buyer_admin_id'].nunique() # 653593           809213
# print train['item_id'].nunique() # 2406722                2812048
# print train['create_order_time'].nunique()  # 2096496      2164403
# print train['irank'].nunique()  # 16790                   42751
# print train.describe()

# irank
# min 1      1
# 25% 4      4
# 50% 8      8
# 75% 15     16
# max 16790   42751
# test表分析
# test_ = pd.read_csv(test_path, encoding='utf-8')
# print len(test_)    #                        166 832
# print test_['buyer_country_id'].nunique() #    1
# print test_['buyer_admin_id'].nunique() #       11398
# print test_['item_id'].nunique() #              104735
# print test_['create_order_time'].nunique()  #    76077
# print test_.describe()



# 看xx国和yy国是否有相同的buyer_admin_id
import numpy as np
# train_xx = train[train.buyer_country_id=='xx']
# unique_xx = train_xx['buyer_admin_id'].unique()
# train_yy = train[train.buyer_country_id=='yy']
# unique_yy = train_yy['buyer_admin_id'].unique()
# a = unique_xx
# b = unique_yy
# print np.sum(a[:min(len(a), len(b))] == b[:min(len(a), len(b))])
# 0 ： 说明两个国家并没有相同的buyer id 存在
# train表没有缺失值，现看attri_表有没有缺失值。 结果:attri表也没有缺失，数据没有缺失值问题
# attr_describe = attr_.describe()
# print 'All missing', np.sum(attr_describe.loc['count'] == 0)
# print 'Seriously missing', np.sum(((attr_describe.loc['count'] <= 250)&(attr_describe.loc['count'] >0)) )
# All missing 0
# Seriously missing 0


# -------------------以下没有进行过


# 现在对train和attr进行merge on item_id以得到用户的总消费额
# item_price_df = attr_[['item_id','item_price']]
# merge_result = pd.merge(train,item_price_df,on='item_id',how='left')
# buyer_spent_sum = merge_result.groupby('buyer_admin_id')['item_price'].sum()
# pd.DataFrame(buyer_spent_sum).to_csv("../../result/buyer_spent_sum.csv")
# buyer_spent_sum = pd.read_csv("../../result/buyer_spent_sum.csv")[['item_price']]
# print buyer_spent_sum.describe()
# min 0
# 25% 377
# 50% 1743
# 75% 4583
# max 4528790

# 对用户所花金额进行直方图展示，可以得到峰度较高的单侧正态分布图
# buyer_spent_sum_sorted = buyer_spent_sum.sort_values('item_price')
# hist = buyer_spent_sum_sorted.iloc[:-5000,:].hist(bins=10)
# import matplotlib.pyplot as plt
# plt.show()
print ""
