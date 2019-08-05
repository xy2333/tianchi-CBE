# 3004.py: 构建测试集的装箱特征
import pandas as pd
df_3001 = pd.read_csv("/home/kesci/work/3001.csv", encoding='utf-8')
df_3002 = pd.read_csv("/home/kesci/work/3002.csv", encoding='utf-8')
df_3003 = pd.read_csv("/home/kesci/work/3003.csv", encoding='utf-8')
merge_1_2_3_test_set = pd.merge(df_3001,df_3002,on='buyer_admin_id',how='inner')
merge_1_2_3_test_set = pd.merge(merge_1_2_3_test_set,df_3003,on='buyer_admin_id',how='inner')

cate_freq = pd.read_csv("/home/kesci/work/2011.csv", encoding='utf-8')
store_freq = pd.read_csv("/home/kesci/work/2012.csv", encoding='utf-8')
del cate_freq['Unnamed: 0'],store_freq['Unnamed: 0']
cate_freq.columns=['fav_cate','cate_freq']
store_freq.columns=['fav_store','store_freq']
# print (merge_1_2_3_test_set.describe())
# 检查测试集和以上表的关联缺失情况
# print (merge_1_2_3_test_set['buyer_admin_id'].nunique()) #11393
merge_result = pd.merge(merge_1_2_3_test_set,cate_freq,on='fav_cate',how='left')
merge_result = pd.merge(merge_result,store_freq,on='fav_store',how='left')
del merge_result['Unnamed: 0'],merge_result['Unnamed: 0_x'],merge_result['Unnamed: 0_y']
# print (merge_result['buyer_admin_id'].nunique())
# 在和频率装箱表的关联过程中，有一些测试集数据发送关联缺失情况 这些数据已经在3000中分析过
# 若提交要求那5个完全缺失的用户的预测值，则随意填充。
# 若不要求，直接用dropna后的构造的特征数据去跑模型
# print (merge_result.describe())
# cate_freq_nan = pd.DataFrame(merge_result[['cate_freq']][merge_result[['cate_freq']].isnull().any(axis=1)])
# cate_freq_nan = cate_freq_nan.reset_index()
# print (cate_freq_nan)
del merge_result['fav_cate'],merge_result['fav_store']
print (merge_result.describe())