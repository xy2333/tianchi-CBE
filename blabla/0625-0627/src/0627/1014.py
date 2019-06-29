# encoding=utf-8

# 查看11776349是否在attr表中真的为NaN
# result: empty 确实是缺失的
import pandas as pd

attri_path = '../../data/0626/Antai_AE_round1_item_attr_20190626.csv'
attr_ = pd.read_csv(attri_path, encoding='utf-8')
t = attr_[attr_.item_id==11776349]
print ""
