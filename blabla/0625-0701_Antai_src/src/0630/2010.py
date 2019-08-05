# 2010.py: 得到每个用户的最后一次购买信息的item_id #test_path =  '../../data/0626/Antai_AE_round1_test_20190626.csv'
#11398
import pandas as pd
test_df = pd.read_csv('/home/kesci/input/data_AE3941/Antai_AE_round1_test_20190626.csv', encoding='utf-8')
test_df = test_df.sort_values(['buyer_admin_id','create_order_time'])
test_df_last_single = test_df.drop_duplicates('buyer_admin_id',keep='last') 
test_df_last_single.to_csv("/home/kesci/work/test_set_last_bought.csv")  #用于之后
print (test_df_last_single.describe())