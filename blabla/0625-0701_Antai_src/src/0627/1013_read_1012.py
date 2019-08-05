#encoding=utf-8
# 读取用户最喜欢的商品类型表
import pandas as pd
buyer_fav_cate_path = '../../result/1012.csv'
buyer_fav_cate = pd.read_csv(buyer_fav_cate_path, encoding='utf-8')
buyer_fav_cate.columns = ['buyer_admin_id',"x",'cate_id']
print buyer_fav_cate.describe()
print ""

# 以下说明 groupby.apply(mode)的结果的中间列意义为：
# [0]时，该用户只有一个cate_id的众数，即单个种类购买最多
# [0,1]时，该用户有两个并列的cate_id的众数，例如买过3次A,3次B，后面的cate_id即这些众数
# [0,1,2]时，该用户有三个并列的....
# train_path = '../../data/0626/Antai_AE_round1_train_20190626.csv'
# train = pd.read_csv(train_path, encoding='utf-8')
# merge_train_attr = pd.read_csv('../../result/1012_train_merge_atti_dropna.csv', encoding='utf-8')
# buyer_detail = train[train.buyer_admin_id==8780885]
# buyer_fav_cate_ = buyer_fav_cate[buyer_fav_cate.buyer_admin_id==8780885]
#
# t_0 = merge_train_attr[merge_train_attr.item_id==790432].iloc[:1,:]
# t_1 = merge_train_attr[merge_train_attr.item_id==4597001].iloc[:1,:]
# t_2 = merge_train_attr[merge_train_attr.item_id==4633909].iloc[:1,:]
# t_3 = merge_train_attr[merge_train_attr.item_id==5351252].iloc[:1,:]
# t_4 = merge_train_attr[merge_train_attr.item_id==5875207].iloc[:1,:]
# t_5 = merge_train_attr[merge_train_attr.item_id==5948177].iloc[:1,:]
# t_6 = merge_train_attr[merge_train_attr.item_id==6024897].iloc[:1,:]
# t_7 = merge_train_attr[merge_train_attr.item_id==7347882].iloc[:1,:]
# t_8 = merge_train_attr[merge_train_attr.item_id==7979097].iloc[:1,:]
# t_9 = merge_train_attr[merge_train_attr.item_id==8244245].iloc[:1,:]
# t_10 = merge_train_attr[merge_train_attr.item_id==8244245].iloc[:1,:]
# t_11 = merge_train_attr[merge_train_attr.item_id==11684798].iloc[:1,:]


train_path = '../../data/0626/Antai_AE_round1_train_20190626.csv'
train = pd.read_csv(train_path, encoding='utf-8')
merge_train_attr = pd.read_csv('../../result/1012_train_merge_atti_dropna.csv', encoding='utf-8')
buyer_detail = train[train.buyer_admin_id==81]
buyer_fav_cate_ = buyer_fav_cate[buyer_fav_cate.buyer_admin_id==81]
t_1 = merge_train_attr[merge_train_attr.item_id==111370].iloc[:1,:]
t_2 = merge_train_attr[merge_train_attr.item_id==3645675].iloc[:1,:]
t_3 = merge_train_attr[merge_train_attr.item_id==4401623].iloc[:1,:]
t_4 = merge_train_attr[merge_train_attr.item_id==7159321].iloc[:1,:]
t_5 = merge_train_attr[merge_train_attr.item_id==9158518].iloc[:1,:]
t_6 = merge_train_attr[merge_train_attr.item_id==9493430].iloc[:1,:]
t_7 = merge_train_attr[merge_train_attr.item_id==10203269].iloc[:1,:]
t_8 = merge_train_attr[merge_train_attr.item_id==11776349].iloc[:1,:]

print ""
