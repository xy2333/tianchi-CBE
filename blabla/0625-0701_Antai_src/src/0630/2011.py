# 2011.py: 构建 cate_id ，cate_freq_id表 表长为3078
cate_freq = pd.DataFrame(merge_1_2_3.groupby(['fav_cate']).size().sort_values(ascending=False)).reset_index()
cate_freq.columns=['fav_cate','cate_occurs'] #'cate_freq_i',
to_join = pd.DataFrame()
for i in range(0,25):
    to_join = to_join.append(pd.DataFrame(np.ones(123)*i))
    if i ==24: # 尾部缓冲处理
        to_join = to_join.append(pd.DataFrame(np.ones(3)*i))
to_join.columns = ['cate_freq_i'] #to_join正常
# to_join的index格式与上面cate_freq的index不同，若不处理会发生问题
df_cate_responding_i = cate_freq.join(to_join.reset_index(drop=True))
del df_cate_responding_i['cate_occurs']
df_cate_responding_i.columns=['cate_id','cate_freq_i']