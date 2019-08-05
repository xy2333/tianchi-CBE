# 3001.py:计算测试集用户最喜欢的商品的类型

# 在上个版本中做了对缺失值的分析，若提交要求那5个完全缺失的用户的预测值，则随意填充。
# 若不要求，直接用此下面构造的特征数据去跑模型

df = pd.read_csv('/home/kesci/input/data_AE3941/Antai_AE_round1_test_20190626.csv', encoding='utf-8')
attr_ = pd.read_csv('/home/kesci/input/data_AE3941/Antai_AE_round1_item_attr_20190626.csv', encoding='utf-8')
all_buy_record = pd.merge(df[['buyer_admin_id','item_id']],attr_[['item_id','cate_id']],on='item_id',how='left')
all_buy_record = all_buy_record.dropna()
buyer_fav_cate = pd.DataFrame(all_buy_record.groupby('buyer_admin_id')['cate_id'].apply(pd.Series.mode)) # 之前在训练集时直接存为csv，免去了将index转换为column的步骤

buyer_fav_cate = buyer_fav_cate.reset_index() # 将带level的index展开为3列
buyer_fav_cate.columns = ['buyer_admin_id',"x",'cate_id']
buyer_fav_cate_single = pd.DataFrame(buyer_fav_cate.groupby('buyer_admin_id')['x'].count())
buyer_fav_cate_single.columns = ['type_count']
# 第一类：将那些只有一个众数的用户提取出来
# 第二类：把有众多众数的用户的favorite设为最后一个购买商品的类型
buyer_fav_cate_single_ = buyer_fav_cate_single[buyer_fav_cate_single.type_count==1] # 第一类
to_be_set_ = buyer_fav_cate_single[buyer_fav_cate_single.type_count!=1]   # 第二类

# 计算第一类结果
buyer_fav_cate_single_ = buyer_fav_cate_single_.reset_index()
merge_single_mode = pd.merge(buyer_fav_cate_single_,buyer_fav_cate,on='buyer_admin_id',how='left')
del merge_single_mode['type_count'],merge_single_mode['x']

# 计算第二类结果
# 对测试集处理，得到每个用户只有最后(datetime)一条记录的的数据
train_df_last_single =  df.sort_values(['buyer_admin_id','create_order_time']).drop_duplicates('buyer_admin_id',keep='last') 
# 将上面第二类和train_df_last_single进行merge
to_be_set_ = to_be_set_.reset_index()
merge_many_mode = pd.merge(to_be_set_,train_df_last_single,on='buyer_admin_id',how='left')
del merge_many_mode['type_count'],merge_many_mode['buyer_country_id'],merge_many_mode['create_order_time'],merge_many_mode['irank']
# 和attri表关联得到cate_id
merge_many_mode = pd.merge(merge_many_mode,attr_,on='item_id',how='left')# ：多众数用户的购买记录左并属性表
del merge_many_mode['item_id'],merge_many_mode['store_id'],merge_many_mode['item_price']# 删去多余特征

# 整合以上两个结果，由此得到所有用户的fav_cate
result = merge_single_mode.append(merge_many_mode)
result.columns = ['buyer_admin_id','fav_cate']
result.to_csv("/home/kesci/work/3001.csv")
# 由下面可以验证确实是那五个用户的缺失
# print (result.describe())  #11393
# print (df['buyer_admin_id'].nunique()) #11398