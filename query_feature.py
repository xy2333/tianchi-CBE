# coding=utf-8
from multiprocessing import Pool
from multiprocessing import cpu_count
import math
import pandas as pd
import datetime
import numpy as np
import gc

processor=cpu_count()-2


# 提取query特征
def query_feature():
    res = []
    p = Pool(processor)
    for i in range(processor):
        res.append(p.apply_async(run_query_feature, args=( i,)))
        print(str(i) + ' processor started !')
    p.close()
    # p.join()：等待所有进程结束之后继续向下进行，用于进程的同步
    p.join()
    data=pd.concat([i.get() for i in res])
    data.to_csv('data/query_all.csv',index=False)

"""
    query特征:
        # 之前之后购买商品的次数
        # 之前之后购买相同商品的次数
        # 之前之后购买相同商品的次数
        # 之前之后购买相同店铺的次数
        # 之前之后购买相同类别的次数
        # 之前之后购买其他商品的次数　
        # 之前之后购买不同商品的种类（不重复）
        # 之前之后购买不同店铺的种类（不重复）
        # 之前之后购买不同种类的种类（不重复）

    """
def run_query_feature(i):
    data=pd.read_csv('data/user_data/query_'+str(i)+'.csv')
    features=[]
    for index,row in data.iterrows():
        feature={}
        feature['instance_id']=row['instance_id']
        if index%100==0:
            print(index)
        col=['buyer_admin_id','create_order_time','day','item_id','store_id','cate_id']
        # 这行用户对应的所有行的信息
        tmp=data[data['buyer_admin_id']==row['buyer_admin_id']][['instance_id']+col]
        # 之前之后购买商品的次数
        before_query_all_cnt=len(tmp[(tmp['create_order_time'] < row['create_order_time'])])
        after_query_all_cnt=len(tmp[(tmp['create_order_time'] > row['create_order_time'])])

        # 之前之后购买相同商品的次数
        before_query_item_cnt=len(tmp[(tmp['item_id'] == row['item_id']) & (tmp['create_order_time'] < row['create_order_time'])])
        after_query_item_cnt=len(tmp[(tmp['item_id'] == row['item_id']) & (tmp['create_order_time'] > row['create_order_time'])])

        # 之前之后购买相同店铺的次数
        before_query_store_cnt=len(tmp[(tmp['store_id'] == row['store_id']) & (tmp['create_order_time'] < row['create_order_time'])])
        after_query_store_cnt=len(tmp[(tmp['store_id'] == row['store_id']) & (tmp['create_order_time'] > row['create_order_time'])])

        # 之前之后购买相同类别的次数
        before_query_cate_cnt=len(tmp[(tmp['cate_id'] == row['cate_id']) & (tmp['create_order_time'] < row['create_order_time'])])
        after_query_cate_cnt=len(tmp[(tmp['cate_id'] == row['cate_id']) & (tmp['create_order_time'] > row['create_order_time'])])

        # 之前之后购买其他商品的次数　
        before_diff_query_cnt = len(set(tmp[(tmp['create_order_time'] < row['create_order_time']) & (tmp['item_id']!=row['item_id'])]))
        after_diff_query_cnt = len(set(tmp[(tmp['create_order_time'] > row['create_order_time']) & (tmp['item_id']!=row['item_id'])]))

        # 最早最晚购买相同商品的时间
        query_min_time=np.min(tmp[(tmp['item_id'] == row['item_id'])]['create_order_time'])
        query_max_time = np.max(tmp[(tmp['item_id'] == row['item_id'])]['create_order_time'])

        # 之前之后购买不同商品的种类（不重复）
        before_query_items= len(set(tmp[(tmp['create_order_time'] < query_min_time)]['item_id']))
        after_query_items= len(set(tmp[(tmp['create_order_time'] > query_max_time)]['item_id']))

        # 之前之后购买不同店铺的种类（不重复）
        before_query_stores= len(set(tmp[(tmp['create_order_time'] < query_min_time)]['store_id']))
        after_query_stores= len(set(tmp[(tmp['create_order_time'] > query_min_time)]['store_id']))

        # 之前之后购买不同种类的种类（不重复）
        before_query_cates= len(set(tmp[(tmp['create_order_time'] < query_min_time)]['cate_id']))
        after_query_cates= len(set(tmp[(tmp['create_order_time'] > query_min_time)]['cate_id']))

        feature['before_query_all_cnt'] = before_query_all_cnt
        feature['after_query_all_cnt'] = after_query_all_cnt

        feature['before_query_item_cnt'] = before_query_item_cnt
        feature['after_query_item_cnt'] = after_query_item_cnt

        feature['before_query_store_cnt'] = before_query_store_cnt
        feature['after_query_store_cnt'] = after_query_store_cnt

        feature['before_query_cate_cnt'] = before_query_cate_cnt
        feature['after_query_cate_cnt'] = after_query_cate_cnt

        feature['before_diff_query_cnt'] = before_diff_query_cnt
        feature['after_diff_query_cnt'] = after_diff_query_cnt

        feature['before_query_items'] = before_query_items
        feature['after_query_items'] = after_query_items

        feature['before_query_stores'] = before_query_stores
        feature['after_query_stores'] = after_query_stores

        feature['before_query_cates'] = before_query_cates
        feature['after_query_stores'] = after_query_stores

        features.append(feature)

    features=pd.DataFrame(features)
    print(features)
    print(str(i) + ' processor finished !')
    return features

print('query_feature start')
query_feature()
print('query_feature finish')