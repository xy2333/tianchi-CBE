import pandas as pd
train_1 = pd.read_csv("../../result/1011_1.csv", encoding='utf-8')
train_2 = pd.read_csv("../../result/1011_2.csv", encoding='utf-8')
# train_path = '../../data/0626/Antai_AE_round1_train_20190626.csv'
# attr_ = pd.read_csv('../../data/0626/Antai_AE_round1_item_attr_20190626.csv' ,encoding="utf-8")

# print train[train.buyer_admin_id==6898295] #224
# print attr_[attr_.item_id==8945882]
# print train_1.describe()
t =  train_1.iloc[-10:,:]
t2 = train_2.iloc[:10,:]
print ""