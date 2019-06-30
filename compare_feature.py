# coding=utf-8
from multiprocessing import Pool
from multiprocessing import cpu_count
import math
import pandas as pd
import datetime
import numpy as np
import gc

processor=cpu_count()-2

# 提取数据
def compare_feature():
    # users = pd.DataFrame(list(set(data['user_id'].values)), columns=['user_id'])
    res = []
    p = Pool(processor)
    for i in range(processor):
        res.append(p.apply_async(run_compare_feature, args=(i,)))
        print(str(i) + ' processor started !')
    p.close()
    p.join()
    data = pd.concat([i.get() for i in res])
    data.to_csv('data/compare_all.csv',index=False)
    # return data

"""
    竞争类特征:
        # 之前之后购买低价商品（不重复）的个数
        # 之前之后购买高价商品（不重复）的个数
        # 之前之后购买低价商品种类（不重复）的个数
        # 之前之后购买高价商品种类（不重复）的个数
        # 之前之后购买低价商品店铺（不重复）的个数
        # 之前之后购买高价商品店铺（不重复）的个数
    
    # origion_data没有加入店铺销量信息，待加入之后再增加以下特征：
        # 之前之后购高销量店铺（不重复）的个数
        # 之前之后购低销量店铺（不重复）的个数

    """

def run_compare_feature(i):
    data = pd.read_csv('data/user_data/query_' + str(i) + '.csv')
    features=[]
    for index,row in data.iterrows():
        feature={}
        feature['instance_id']=row['instance_id']
        if index%1000==0:
            print(index)
        col=['buyer_admin_id','create_order_time','day','item_id','store_id','cate_id','item_price']
        tmp=data[data['buyer_admin_id']==row['buyer_admin_id']][['instance_id']+col]
        # tmp=tmp.sort_values(by='context_timestamp').reset_index(drop=True)

        # 之前之后购买低价商品（不重复）的个数
        before_low_price_cnt=len(set(tmp[(tmp['create_order_time']<row['create_order_time']) &(tmp['item_price']<row['item_price'])]['item_id']))
        after_low_price_cnt=len(set(tmp[(tmp['create_order_time']>row['create_order_time']) &(tmp['item_price']<row['item_price'])]['item_id']))

        # 之前之后购买高价商品（不重复）的个数
        before_high_price_cnt=len(set(tmp[(tmp['create_order_time']<row['create_order_time']) &(tmp['item_price']>row['item_price'])]['item_id']))
        after_high_price_cnt=len(set(tmp[(tmp['create_order_time']>row['create_order_time']) &(tmp['item_price']>row['item_price'])]['item_id']))

        # 之前之后购买低价商品种类（不重复）的个数
        before_low_price_cates=len(set(tmp[(tmp['create_order_time']<row['create_order_time']) &(tmp['item_price']<row['item_price'])]['cate_id']))
        after_low_price_cates=len(set(tmp[(tmp['create_order_time']>row['create_order_time']) &(tmp['item_price']<row['item_price'])]['cate_id']))

        # 之前之后购买高价商品种类（不重复）的个数
        before_high_price_cates=len(set(tmp[(tmp['create_order_time']<row['create_order_time']) &(tmp['item_price']>row['item_price'])]['cate_id']))
        after_high_price_cates=len(set(tmp[(tmp['create_order_time']>row['create_order_time']) &(tmp['item_price']>row['item_price'])]['cate_id']))

        # 之前之后购买低价商品店铺（不重复）的个数
        before_low_price_stores=len(set(tmp[(tmp['create_order_time']<row['create_order_time']) &(tmp['item_price']<row['item_price'])]['store_id']))
        after_low_price_stores=len(set(tmp[(tmp['create_order_time']>row['create_order_time']) &(tmp['item_price']<row['item_price'])]['store_id']))

        # 之前之后购买高价商品店铺（不重复）的个数
        before_high_price_stores=len(set(tmp[(tmp['create_order_time']<row['create_order_time']) &(tmp['item_price']>row['item_price'])]['store_id']))
        after_high_price_stores=len(set(tmp[(tmp['create_order_time']>row['create_order_time']) &(tmp['item_price']>row['item_price'])]['store_id']))

        # origion_data没有加入店铺销量信息，待加入之后再增加以下特征
        # 之前之后购高销量店铺（不重复）的个数
        # 之前之后购低销量店铺（不重复）的个数

        feature['before_low_price_cnt'] = before_low_price_cnt
        feature['after_low_price_cnt'] = after_low_price_cnt

        feature['before_high_price_cnt'] = before_high_price_cnt
        feature['after_high_price_cnt'] = after_high_price_cnt

        feature['before_low_price_cates'] = before_low_price_cates
        feature['after_low_price_cates'] = after_low_price_cates

        feature['before_high_price_cates'] = before_high_price_cates
        feature['after_high_price_cates'] = after_high_price_cates

        feature['before_low_price_stores'] = before_low_price_stores
        feature['after_low_price_stores'] = after_low_price_stores

        feature['before_high_price_stores'] = before_high_price_stores
        feature['after_high_price_stores'] = after_high_price_stores


        features.append(feature)
    print(str(i) + ' processor finished !')
    return pd.DataFrame(features)



print('compare_feature start')
compare_feature()
print('compare_feature finish')