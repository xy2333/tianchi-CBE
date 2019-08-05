# 2007.py:对fav_store进行初步装箱并 对训练集将fav_cate和fav_store按频率装箱
df1 = pd.read_csv("/home/kesci/work/2001.csv", encoding='utf-8')
df2 = pd.read_csv("/home/kesci/work/2002.csv", encoding='utf-8')
df3 = pd.read_csv("/home/kesci/work/2003.csv", encoding='utf-8')
merge_1_2 = pd.merge(df1,df2,on='buyer_admin_id',how='inner')
merge_1_2_3 = pd.merge(merge_1_2,df3,on='buyer_admin_id',how='inner')
result = pd.merge(merge_1_2_3,train_df_last_single[['buyer_admin_id','item_id']],on='buyer_admin_id',how='left')
del result['Unnamed: 0_x'],result['Unnamed: 0_y'],result['Unnamed: 0']     
# print (result.info())
# 把fav_cate的值转换成按频率装箱后的i 
result = pd.merge(result,df_cate_responding_i,left_on='fav_cate',right_on='cate_id',how='left')
# print (result.info())
del result['fav_cate'],result['cate_id']
result = result.rename(columns={'cate_freq_i': 'fav_cate'})
# print (result.head())

# 对item_id转换->对应cate_id->对应装箱的cate_freq_i
# 1. item_id转换->对应cate_id
attr_ = pd.read_csv( '/home/kesci/input/data_AE3941/Antai_AE_round1_item_attr_20190626.csv', encoding='utf-8')
result = pd.merge(result,attr_,on='item_id', how='left')
# print (result.head())
# 2. 对应cate_id->对应装箱的cate_freq_i
result = pd.merge(result,df_cate_responding_i,on='cate_id',how='left')
del result['item_id'],result['cate_id'],result['item_price'],result['store_id']
result = result.rename(columns={'cate_freq_i': 'y_freq_i'})     #
# print (result.describe()) y全为0

# 将fav_store的store进行初步装箱
# print (result['fav_store'].nunique()) #52627
store_freq = pd.DataFrame(merge_1_2_3.groupby(['fav_store']).size().sort_values(ascending=False)).reset_index()
to_join = pd.DataFrame()

for i in range(0,25):
    to_join = to_join.append(pd.DataFrame(np.ones(2105)*i))
    if i ==24: # 尾部缓冲处理
        to_join = to_join.append(pd.DataFrame(np.ones(2)*i))
# to_join.columns = ['store_freq_i']
# to_join的index格式与上面cate_freq的index不同，若不处理会发生问题
# print (len(store_freq))
# print (len(to_join))
# print (store_freq.head())
# print (to_join.head())

store_freq = store_freq[['fav_store']].join(to_join.reset_index(drop=True)) 
df_store_responding_i = store_freq
df_store_responding_i.columns=['fav_store','store_freq_i']


# 对训练集进行fav_store 的merge
# print (result.head())
result = pd.merge(result,df_store_responding_i,on='fav_store',how='left')
del result['fav_store']
result = result.rename(columns={'store_freq_i': 'fav_store'})
