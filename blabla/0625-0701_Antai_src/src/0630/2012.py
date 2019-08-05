# 2012.py:构建fav_store store_freq_i
# print (result['fav_store'].nunique()) #52627
store_freq = pd.DataFrame(merge_1_2_3.groupby(['fav_store']).size().sort_values(ascending=False)).reset_index()
to_join = pd.DataFrame()

for i in range(0,25):
    to_join = to_join.append(pd.DataFrame(np.ones(2105)*i))
    if i ==24: # 尾部缓冲处理
        to_join = to_join.append(pd.DataFrame(np.ones(2)*i))
store_freq = store_freq[['fav_store']].join(to_join.reset_index(drop=True)) 
df_store_responding_i = store_freq
df_store_responding_i.columns=['fav_store','store_freq_i']
