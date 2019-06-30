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
def leak_feature():
    res = []
    p = Pool(processor)
    for i in range(processor):
        res.append(p.apply_async(run_leak_feature, args=( i,)))
        print(str(i) + ' processor started !')
    p.close()
    p.join()
    data = pd.concat([i.get() for i in res])
    data.to_csv('data/leak_all.csv',index=False)
    # return data

"""
    购买间隔类特征:
        # 购买时间间隔统计数据（最大值;最小值;中位数;平均数）
        # 第一次/最后一次购买和当前相距时间
        # 最近上一次下一次购买和当前相距时间
        # 之前之后购买次数所占的比例
        # 之前之后购买商品（不重复）所占的比例
        # 之前之后购买商铺（不重复）所占的比例
        # 之前之后购买商品种类（不重复）所占的比例
    
    """
def sec_diff(a,b):
    if (a is np.nan) | (b is np.nan):
        return -1
    # striptime:将时间解析成元组，包含日期月份小时等信息
    # return (datetime.datetime.strptime(str(b), "%Y-%m-%d %H:%M:%S")-datetime.datetime.strptime(str(a), "%Y-%m-%d %H:%M:%S")).seconds
    return (datetime.datetime.strptime(str(b), "%Y-%m-%d %H:%M:%S")-datetime.datetime.strptime(str(a), "%Y-%m-%d %H:%M:%S")).total_seconds()

def run_leak_feature(i):
    col = ['buyer_admin_id', 'create_order_time', 'day', 'item_id', 'store_id', 'cate_id']

    # col = ['user_id', 'predict_category_property', 'context_timestamp', 'day', 'query1', 'query', 'item_id', 'shop_id',
    #        'item_brand_id', 'item_city_id', 'item_category_list']
    data = pd.read_csv('data/user_data/query_' + str(i) + '.csv')[['instance_id']+col]
    features=[]
    # query对每一行处理
    # 每一行存成一个字典
    for index, row in data.iterrows():
        feature={}
        feature['instance_id']=row['instance_id']
        if index%1000==0:
            print(index)
        # tmp = data[(data['user_id'] == row['user_id'])&(data['day']==row['day'])]
        tmp = data[(data['buyer_admin_id'] == row['buyer_admin_id'])]
        # drop:落下（drop = True :在原有的索引上修改）
        # sort_value:默认升序
        tmp=tmp.sort_values(by='create_order_time').reset_index(drop=True)
        diffs=[]
        if len(tmp)==1:
            diffs.append(-1)
        else:
            for ind in range(len(tmp)-1):
                # diffs.append(sec_diff(tmp.loc[ind+1,'create_order_time'],tmp.loc[ind,'create_order_time']))
                diffs.append(sec_diff(tmp.loc[ind,'create_order_time'],tmp.loc[ind+1,'create_order_time']))
        # 购买时间间隔统计数据
        max_diff=np.max(diffs)
        min_diff=np.min(diffs)
        avg_diff=np.mean(diffs)
        mid_diff=np.median(diffs)

        # 第一次/最后一次购买和当前相距时间
        # diff_first_click:正
        diff_first_click=sec_diff(tmp.loc[0,'create_order_time'],row['create_order_time'])
        diff_last_click = sec_diff(row['create_order_time'], tmp.loc[len(tmp)-1, 'create_order_time'])

        # 最近上一次下一次购买和当前相距时间
        previous_diff=sec_diff( np.max(tmp[(tmp['create_order_time'] < row['create_order_time'])]['create_order_time']),row['create_order_time'])
        next_diff=sec_diff(row['create_order_time'],np.min(tmp[(tmp['create_order_time'] > row['create_order_time'])]['create_order_time']))

        query_cnt=len(tmp)
        # 之前之后购买次数所占的比例
        before_query_rate=len(tmp[(tmp['create_order_time']<=row['create_order_time'])])/query_cnt
        after_query_rate=1-before_query_rate

        item_cnt=len(set(tmp['item_id']))
        # 之前之后购买商品（不重复）所占的比例
        before_item_rate=len(set(tmp[(tmp['create_order_time']<=row['create_order_time'])]['item_id']))/item_cnt
        after_item_rate=1-before_item_rate

        store_cnt=len(set(tmp['store_id']))
        # 之前之后购买商铺（不重复）所占的比例
        before_store_rate=len(set(tmp[(tmp['create_order_time']<=row['create_order_time'])]['store_id']))/store_cnt
        after_store_rate=1-before_store_rate

        cate_cnt=len(set(tmp['cate_id']))
        # 之前之后购买商品种类（不重复）所占的比例
        before_cate_rate=len(set(tmp[(tmp['create_order_time']<=row['create_order_time'])]['cate_id']))/cate_cnt
        after_cate_rate=1-before_cate_rate

        feature['max_diff'] = max_diff
        feature['min_diff'] = min_diff
        feature['avg_diff'] = avg_diff
        feature['mid_diff'] = mid_diff

        feature['diff_first_click'] = diff_first_click
        feature['diff_last_click'] = diff_last_click

        feature['previous_diff'] = previous_diff
        feature['next_diff'] = next_diff

        feature['before_query_rate'] = before_query_rate
        feature['after_query_rate'] = after_query_rate

        feature['before_item_rate'] = before_item_rate
        feature['after_item_rate'] = after_item_rate

        feature['before_store_rate'] = before_store_rate
        feature['after_store_rate'] = after_store_rate

        feature['before_cate_rate'] = before_cate_rate
        feature['after_cate_rate'] = after_cate_rate


        # feature是字典;features是list
        features.append(feature)
    print(str(i) + ' processor finished !')
    return pd.DataFrame(features)


print('leak_feature start')
leak_feature()
print('leak_feature finish')