# 3000.py：对测试集的缺失数据进行分析
import pandas as pd
# 读取测试集和属性表
df = pd.read_csv('/home/kesci/input/data_AE3941/Antai_AE_round1_test_20190626.csv', encoding='utf-8')
attr_ = pd.read_csv('/home/kesci/input/data_AE3941/Antai_AE_round1_item_attr_20190626.csv', encoding='utf-8')
# print (df.sort_values('buyer_admin_id').iloc[:50])
# 测试集中每个用户都有7条数据吗:没错 至少都有7条，min=7
# group_ = df.groupby('buyer_admin_id')['item_id'].count()
# print (group_.describe())#都有7条，min=7
# 测试集中的数据有些和attri表中对不上，这些NaN的数据对应的buyer_admin_id的结果需要提交吗？
all_buy_record = pd.merge(df[['buyer_admin_id','item_id']],attr_[['item_id','cate_id']],on='item_id',how='left')
cate_nan = all_buy_record[all_buy_record.isnull().any(axis=1)] 
# print (cate_nan.describe())# 有674条nan记录
# print (cate_nan.groupby('buyer_admin_id')['item_id'].count().describe())
# 有360位用户的购买的商品对应的商品类型缺失，检查其中超过7条缺失的用户
cate_nan_count = pd.DataFrame(cate_nan.groupby('buyer_admin_id')['item_id'].count()).reset_index()
cate_nan_count.columns = ['buyer_admin_id','nan_count']
need_check = cate_nan_count[cate_nan_count.nan_count>=7]
need_check_records = pd.merge(all_buy_record,need_check,on='buyer_admin_id',how="inner")
# 要确保这些超过7条缺失的用户全都至少有一条不缺失的记录
# print (len(need_check)) #有14个用户need check
those_for_sure = need_check_records.dropna().drop_duplicates('buyer_admin_id')
# print (len(those_for_sure)) #有9位用户至少有一条不缺失的记录，他们可以直接训练
those_for_sure_list = those_for_sure['buyer_admin_id'].values
# 以下是完全缺失的
complete_nan = need_check[~need_check['buyer_admin_id'].isin(those_for_sure_list)]
record_ = pd.merge(all_buy_record,complete_nan,on='buyer_admin_id',how='inner')