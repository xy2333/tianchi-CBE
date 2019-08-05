# 3011.py:处理3006中的label 并作为y_label, merge到3010(装箱后)的结果中 直接将item_id设置为y_label
import pandas as pd
# xx_train_y = pd.read_csv("/home/kesci/work/3006_xx_train_y.csv", encoding='utf-8')[['buyer_admin_id','item_id']] # 670 562个unique item
xx_train_X_handled = pd.read_csv("/home/kesci/work/3010.csv", encoding='utf-8')
# print (xx_train_X_handled['buyer_admin_id'].nunique())
# print (xx_train_y['buyer_admin_id'].unique()) 
# 考虑缺失和不匹配
# isin_ = xx_train_X_handled['buyer_admin_id'].isin(xx_train_y['buyer_admin_id'].unique())
# print (pd.DataFrame(isin_).reset_index().groupby('buyer_admin_id')['buyer_admin_id'].count())
# 有69个不匹配： 对于所有xx_train_y的buyer_admin_id去对应标签，有69个标签缺失。
# 缺失情况在3000中分析过
# 若提交要求完全缺失的用户的预测值，则随意填充。
# 若不要求，直接用dropna后的构造的特征数据去跑模型。
# 目前直接dropna用完全不缺失的用户来构建
xx_train_y.columns = ['buyer_admin_id','y_item_id']
merge_result = pd.merge(xx_train_X_handled,xx_train_y,on='buyer_admin_id',how='left')
merge_result = merge_result.dropna()
merge_result.to_csv("/home/kesci/work/3011.csv")
# print (merge_result.describe())