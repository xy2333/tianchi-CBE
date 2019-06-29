#encoding=utf-8
# 读取用户最喜欢的商品类型表
import pandas as pd
buyer_fav_cate_path = '../../result/1012.csv'
buyer_fav_cate = pd.read_csv(buyer_fav_cate_path, encoding='utf-8')
buyer_fav_cate.columns = ['buyer_admin_id',"x",'cate_id']
single = buyer_fav_cate[buyer_fav_cate.x==0]
print single.describe()
print ""