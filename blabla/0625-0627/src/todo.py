#todo:
# 0. 计算用户最喜欢的商品的类型，最喜欢的商铺 1005
#   0.1.如果对用户购买商品的种类的众数进行特征构建，单个用户可能买了若干种类的商品，如何处理？
#   考虑那些众数为1个的用户，构建他们的favorite商品类型，对于其他用户用缺失代替,但对于标签数据的缺失值怎么处理？（尝试去看lightgbm的标签数据缺失填充方法）
# 1： 购买水平的时序建模
#   构建一个横轴为购买次序，纵轴为购买内容（物品Id,金额)
#   尝试将此时序模型做平稳性分析并ARMA建模
# 2. 统计用户的购买数据
#   buyer_admin_id用groupby进行特征构建
#   buy_sum,buy_count,buy_category
#   怎样一种推荐购买算法？ 昂贵的？ 便宜的？ 买的多的？ 加权？
#   先统计出不同用户目前已经花费的金额（sum) 然后该人群进行分布统计（KDE图）

# 先计算这些统计数据 然后对xx国的用户进行建模
# done:
1. 看sklearn.importantce （看不了，目前数据集不完整）
2. train表中的time数据的转换 1002
isweekend? isweekday? ismorning? isafternoon? isnight? ismiddlenight?
                      5:00-11:00  11:00-17:00 17:00-23:00 23:00-5:00
 更进一步： 统计 用户 在morning,afternoon,night,midnight购物的比例 1004
