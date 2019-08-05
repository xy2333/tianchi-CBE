import pandas as pd
attri_path = '../../data/0626/Antai_AE_round1_item_attr_20190626.csv'
attr_ = pd.read_csv(attri_path, encoding='utf-8')
t1 = attr_.groupby('store_id')['item_price'].unique()
print ""