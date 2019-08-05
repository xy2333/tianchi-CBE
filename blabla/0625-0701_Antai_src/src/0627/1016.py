#encoding=utf-8
# 处理train表：每个buyer保留最后一个datetime记录
import pandas as pd
train_path = "../../data/0626/Antai_AE_round1_train_20190626.csv"
train_df = pd.read_csv(train_path, encoding='utf-8')
train_df = train_df.sort_values(['buyer_admin_id','create_order_time'])
train_df = train_df.drop_duplicates('buyer_admin_id',keep='last')
print ""