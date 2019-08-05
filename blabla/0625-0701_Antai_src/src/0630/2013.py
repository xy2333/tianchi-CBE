# 2013.py:开始对测试集进行merge 确保最后长度为166 832
result = pd.merge(merge_1_2_3,test_df_last_single[['buyer_admin_id','item_id']],on='buyer_admin_id',how='left')
del result['Unnamed: 0_x'],result['Unnamed: 0_y'],result['Unnamed: 0']   
# 把fav_cate的值转换成按频率装箱后的i 
result = pd.merge(result,df_cate_responding_i,left_on='fav_cate',right_on='cate_id',how='left')
del result['fav_cate'],result['cate_id']
result = result.rename(columns={'cate_freq_i': 'fav_cate'})

# 对item_id转换->对应cate_id->对应装箱的cate_freq_i
# 1. item_id转换->对应cate_id
attr_ = pd.read_csv( '/home/kesci/input/data_AE3941/Antai_AE_round1_item_attr_20190626.csv', encoding='utf-8')
result = pd.merge(result,attr_,on='item_id', how='left')
# print (result.head())
# 2. 对应cate_id->对应装箱的cate_freq_i
result = pd.merge(result,df_cate_responding_i,on='cate_id',how='left')
del result['item_id'],result['cate_id'],result['item_price'],result['store_id']
result = result.rename(columns={'cate_freq_i': 'y_freq_i'})


# 对训练集进行fav_store 的merge
# print (result.head())
result = pd.merge(result,df_store_responding_i,on='fav_store',how='left')
del result['fav_store']
result = result.rename(columns={'store_freq_i': 'fav_store'})