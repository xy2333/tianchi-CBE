import numpy as np
import pandas as pd
import os
from tqdm import tqdm_notebook
import lightgbm as lgb
import xgboost as xgb
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.filterwarnings('ignore')

item = pd.read_csv("../../data/0626/Antai_AE_round1_item_attr_20190626.csv")
# submit = pd.read_csv(path+'Antai_AE_round1_submit_20190715.csv', header=None)
test = pd.read_csv('../../result/3040xx_train_X.csv')
train = pd.read_csv('../../data/0626/Antai_AE_round1_train_20190626.csv')

def get_preprocessing(df_):
    df = df_.copy()
    df['hour'] = df['create_order_time'].apply(lambda x: int(x[11:13]))
    df['day'] = df['create_order_time'].apply(lambda x: int(x[8:10]))
    df['month'] = df['create_order_time'].apply(lambda x: int(x[5:7]))
    df['year'] = df['create_order_time'].apply(lambda x: int(x[0:4]))
    df['date'] = (df['month'].values - 7) * 31 + df['day']
    del df['create_order_time']
    return df


train = get_preprocessing(train)
test = get_preprocessing(test)

# 高频item_id
temp = train.loc[train.buyer_country_id == 'xx']
# 将同个用户购买的同个商品reduce为1
temp = temp.drop_duplicates(subset=['buyer_admin_id', 'item_id'], keep='first')
item_cnts = temp.groupby(['item_id']).size().reset_index()
item_cnts.columns = ['item_id', 'cnts']
item_cnts = item_cnts.sort_values('cnts', ascending=False)
items = item_cnts['item_id'].values.tolist()


# 很多admin的历史行为不够30个item，所以就需要填充够30个
# 这里使用train下yy的数据构造item_id频次排序，然后依次填充
def item_fillna(tmp_):
    tmp = tmp_.copy()
    l = len(tmp)
    if l == 30:
        tmp = tmp
    elif l < 30:
        m = 30 - l
        items_t = items.copy()
        for i in range(m):
            for j in range(50):
                it = items_t.pop(0)
                if it not in tmp:
                    tmp.append(it)
                    break
    elif l > 30:
        tmp = tmp[:30]

    return tmp


# 获取top30的item
def get_item_list(df_):
    df = df_.copy()
    dic = {}
    flag = 0
    tt = df[['buyer_admin_id', 'item_id']].values
    for item in df[['buyer_admin_id', 'item_id']].values:
        try:
            dic[item[0]].append(item[1])  # try在以下情况出现except: dict[key]中key不存在，也就是item[0]不存在时。
            #也就是 dict出现新值时：#1.第一个值 #2.之后新值时
        except:
            if flag != 0: # dict出现新值时且#2.之后新值时
                # 去重
                tmp = []
                for i in dic[flag]:
                    if i not in tmp:
                        tmp.append(i)
                # 填充
                tmp = item_fillna(tmp)
                dic[flag] = tmp
                flag = item[0]
            else: # dict出现新值时：#1.第一个值
                flag = item[0]
            dic[item[0]] = [item[1]]

    return dic

# 使用yy国的历史购买记录填充，test是yy国b部分用户购买数据除去最后一条
test = test.sort_values(['buyer_admin_id', 'irank'])
dic = get_item_list(test)
# {152: [8410857, 7937154, 8472223, 4016066, 9891513, 8064216, 8351840, 12824199, 12891086, 12673275, 12807295, 12049470, 12691565, 12817558, 7668726, 7163049, 10266898, 7198434, 9958362, 9722278, 10027998, 1933438, 4203956, 12860885, 12055637, 12869145, 12887251, 1130997, 9951478, 7223628], 282: [11721802, 7665423, 10808393, 11310708, 623582, 6547607, 2605373, 688799, 10517456, 9677940, 11536575, 4724392, 12824199, 12891086, 12673275, 12807295, 12049470, 12691565, 12817558, 7668726, 7163049, 10266898, 7198434, 9958362, 9722278, 10027998, 1933438, 4203956, 12860885, 12055637],
# 最终提交
temp = pd.DataFrame({'lst': dic}).reset_index() # column: index;1st[item_list]      152:
for i in range(30):
    temp[i] = temp['lst'].apply(lambda x: x[i])
del temp['lst']
temp.to_csv('submission.csv', index=False, header=None)