# 3006.py: 对训练集进行处理：只使用XX国家的所有数据，再去掉每个用户最后一条数据，将其作为标签
import pandas as pd
train_df = pd.read_csv('/home/kesci/input/data_AE3941/Antai_AE_round1_train_20190626/Antai_AE_round1_train_20190626.csv', encoding='utf-8')
# 划分开 xx 和 yy 两个国家的数据：10 635 642+2 232 867=12 868 509
train_xx = train_df[train_df['buyer_country_id'] == 'xx']
train_yy = train_df[train_df['buyer_country_id'] == 'yy']
# 训练集本身没有缺失，划分国家后，每个用户至少有8条记录，可以放心去掉最后一条当作标签
# group_ = train_xx.dropna().groupby('buyer_admin_id')['item_id'].count()
# print (group_.describe())
# group_ = train_xx.groupby('buyer_admin_id')['item_id'].count()
# print (group_.describe())
# group_ = train_yy.dropna().groupby('buyer_admin_id')['item_id'].count()
# print (group_.describe())
# group_ = train_yy.groupby('buyer_admin_id')['item_id'].count()
# print (group_.describe())
# 由于irank不对后续特征构建产生影响，而在测试集中 irank是2，3，4，5.。，直接去除即可。
# df = pd.read_csv('/home/kesci/input/data_AE3941/Antai_AE_round1_test_20190626.csv', encoding='utf-8')
# group_ = df.groupby('buyer_admin_id')['irank'].count()
# print (df.sort_values('irank').iloc[:50]) # irank的确最小是2 
# 将最后一条剔除为label_y
xx_train_X = train_xx[train_xx['irank'] != 1]
xx_train_y = train_xx[train_xx['irank'] == 1]
xx_train_X.to_csv("/home/kesci/work/3006_xx_train_X.csv")
xx_train_y.to_csv("/home/kesci/work/3006_xx_train_y.csv")
