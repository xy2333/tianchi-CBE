#2005.py:得到每个用户的最后一次购买信息的item_id
import pandas as pd
train_df = pd.read_csv('/home/kesci/input/data_AE3941/Antai_AE_round1_train_20190626/Antai_AE_round1_train_20190626.csv', encoding='utf-8')
train_df = train_df.sort_values(['buyer_admin_id','create_order_time'])
train_df_last_single = train_df.drop_duplicates('buyer_admin_id',keep='last') 
train_df_last_single.to_csv("/home/kesci/work/2005.csv")  #用于2008.py
