# 3010.py: 构建3006训练集的装箱特征 数据为已经剔除最后一条的数据
import pandas as pd
import numpy as np
import math
df_3001 = pd.read_csv("/home/kesci/work/3007.csv", encoding='utf-8')
df_3002 = pd.read_csv("/home/kesci/work/3008.csv", encoding='utf-8')
df_3003 = pd.read_csv("/home/kesci/work/3009.csv", encoding='utf-8')
merge_1_2_3_train_set = pd.merge(df_3001,df_3002,on='buyer_admin_id',how='inner')
merge_1_2_3_train_set = pd.merge(merge_1_2_3_train_set,df_3003,on='buyer_admin_id',how='inner')


# 构建 df_cate_responding_i 
cate_freq = pd.DataFrame(merge_1_2_3_train_set.groupby(['fav_cate']).size().sort_values(ascending=False)).reset_index()
cate_freq.columns=['fav_cate','cate_occurs'] #'cate_freq_i',
len_cate_freq = len(cate_freq)
len_cate_freq_divided_by_25 = math.floor(len_cate_freq/25)
residual = len_cate_freq-len_cate_freq_divided_by_25*25
to_join = pd.DataFrame()
for i in range(0,25):
    to_join = to_join.append(pd.DataFrame(np.ones(len_cate_freq_divided_by_25)*i))
    if i ==24: # 尾部缓冲处理
        to_join = to_join.append(pd.DataFrame(np.ones(residual)*i))
to_join.columns = ['cate_freq_i'] #to_join正常
# to_join的index格式与上面cate_freq的index不同，若不处理会发生问题
df_cate_responding_i = cate_freq.join(to_join.reset_index(drop=True))
del df_cate_responding_i['cate_occurs']
df_cate_responding_i.columns=['cate_id','cate_freq_i']

# 构建df_store_responding_i
store_freq = pd.DataFrame(merge_1_2_3_train_set.groupby(['fav_store']).size().sort_values(ascending=False)).reset_index()
len_store_freq = len(store_freq)
len_store_freq_divided_by_25 = math.floor(len_store_freq/25)
residual = len_store_freq-len_store_freq_divided_by_25*25
to_join = pd.DataFrame()
for i in range(0,25):
    to_join = to_join.append(pd.DataFrame(np.ones(len_store_freq_divided_by_25)*i))
    if i ==24: # 尾部缓冲处理
        to_join = to_join.append(pd.DataFrame(np.ones(residual)*i))
store_freq = store_freq[['fav_store']].join(to_join.reset_index(drop=True)) 
df_store_responding_i = store_freq
df_store_responding_i.columns=['fav_store','store_freq_i']

# 使用上面构造的两个表进行装箱
cate_freq = df_cate_responding_i
store_freq = df_store_responding_i
cate_freq.columns=['fav_cate','cate_freq']
store_freq.columns=['fav_store','store_freq']

merge_result = pd.merge(merge_1_2_3_train_set,cate_freq,on='fav_cate',how='left')
merge_result = pd.merge(merge_result,store_freq,on='fav_store',how='left')
# 将没有用的column全部del掉
del merge_result['Unnamed: 0'],merge_result['Unnamed: 0_x'],merge_result['Unnamed: 0_y']
del merge_result['fav_cate'],merge_result['fav_store']
merge_result = merge_result.rename(columns={'cate_freq':'fav_cate','store_freq':'fav_store'}) 
# 在和频率装箱表的关联过程中，有一些测试集数据发送关联缺失情况 这些数据已经在3000中分析过
# 若提交要求那5个完全缺失的用户的预测值，则随意填充。
# 若不要求，直接用dropna后的构造的特征数据去跑模型
print (merge_result.describe())
merge_result.to_csv("/home/kesci/work/3010.csv")

