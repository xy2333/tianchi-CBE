# 2009.py 得到训练集的特征集合
df1 = pd.read_csv("/home/kesci/work/2001.csv", encoding='utf-8')
df2 = pd.read_csv("/home/kesci/work/2002.csv", encoding='utf-8')
df3 = pd.read_csv("/home/kesci/work/2003.csv", encoding='utf-8')
merge_1_2 = pd.merge(df1,df2,on='buyer_admin_id',how='inner')
merge_1_2_3 = pd.merge(merge_1_2,df3,on='buyer_admin_id',how='inner')