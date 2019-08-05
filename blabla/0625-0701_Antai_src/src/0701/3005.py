# 3005 进行lightgbm对训练集的预测 CV 早停
import pandas as pd
result = pd.read_csv("/home/kesci/work/2007.csv",encoding="utf-8")
result = result.dropna()

from sklearn.model_selection import train_test_split
data_ = result[['is_morning','is_afternoon','is_night', 'is_midnight', 'fav_cate','fav_store']]
target_ = result[['y_freq_i']]
X_train,X_test,y_train,y_test =train_test_split(data_,target_,test_size=0.2)
import lightgbm as lgb
from sklearn.metrics import mean_squared_error
# y_train['y_freq_i'] = y_train['y_freq_i'].apply(int)
# y_test['y_freq_i'] = y_test['y_freq_i'].apply(int)
print (X_train)
lgb_train = lgb.Dataset(X_train, y_train.values.reshape(-1),feature_name=['is_morning','is_afternoon','is_night', 'is_midnight'],categorical_feature=['y_freq_i','fav_store', 'fav_cate'])

lgb_eval = lgb.Dataset(X_test, y_test.values.reshape(-1), reference=lgb_train,feature_name=['is_morning','is_afternoon','is_night', 'is_midnight'],categorical_feature=[ 'fav_cate','fav_store','y_freq_i'])  # 创建验证数据
params = {  #TypeError: Wrong type(str) or unknown name(y_freq_i) in categorical_feature
    'task': 'train',
    'boosting_type': 'gbdt',  # 设置提升类型
    'objective': 'multiclass', # 目标函数
    'metric': {'l2', 'auc'},  # 评估函数
    'num_leaves': 31,   # 叶子节点数
    'learning_rate': 0.05,  # 学习速率
    'feature_fraction': 0.9, # 建树的特征选择比例
    'bagging_fraction': 0.8, # 建树的样本采样比例
    'bagging_freq': 5,  # k 意味着每 k 次迭代执行bagging
    'verbose': 1 # <0 显示致命的, =0 显示错误 (警告), >0 显示信息
}
print('Start training...')
# 训练 cv and train ，The model will train until the validation score stops improving.
gbm = lgb.train(params,lgb_train,num_boost_round=20,valid_sets=lgb_eval,early_stopping_rounds=5) # 训练数据需要参数列表和数据集
print('Start predicting...')
# 预测数据集
y_pred = gbm.predict(X_test, num_iteration=gbm.best_iteration) #如果在训练期间启用了早期停止，可以通过best_iteration方式从最佳迭代中获得预测
# 评估模型
print('The rmse of prediction is:', mean_squared_error(y_test, y_pred) ** 0.5) # 计算真实值和预测值之间的均方根误差