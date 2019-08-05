todo:
0. 标签型数据 种类过多的问题 lightgbm里要求对其进行降低基数
       
LightGBM/examples at master · microsoft/LightGBM · GitHub
https://github.com/microsoft/LightGBM/tree/master/examples

0.2 python机器学习实战  第一部分：分类
       0.3 现在在看sklearn的lda过程 https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html
先计算这些统计数据 然后对xx国的用户进行建模
Sunil Ray, Author at Analytics Vidhya - Page 2 of 8
https://www.analyticsvidhya.com/blog/author/sunil-ray/page/2/
1： 购买水平的时序建模
  构建一个横轴为购买次序，纵轴为购买内容（物品Id,金额)
  尝试将此时序模型做平稳性分析并ARMA建模
2. 统计用户的购买能力水平
  buyer_admin_id用groupby进行特征构建
  buy_sum,buy_count,buy_category
  怎样一种推荐购买算法？ 昂贵的？ 便宜的？ 买的多的？ 加权？
  先统计出不同用户目前已经花费的金额（sum) 然后该人群进行分布统计（KDE图）
3.python数据科学手册
4.python机器学习实战:MapReduce

0.1 主成分分析（r 语言实战) PCA无法解决高基数问题

8 Proven Ways for boosting the "Accuracy" of a Machine Learning Model
https://www.analyticsvidhya.com/blog/2015/12/improve-machine-learning-results/

SAS Macros For Faster Data Manipulation Complete Tutorial
https://www.analyticsvidhya.com/blog/2015/12/complete-tutorial-sas-macros-faster-data-manipulation/

catboost没有直接对categorical features with high cardinality处理的api，待考虑
catboost 
Jupyter Notebook
https://catboost.ai/docs/features/visualization_jupyter-notebook.html#visualization_jupyter-notebook
CatBoost: Machine learning library to handle categorical data automatically
https://www.analyticsvidhya.com/blog/2017/08/catboost-automated-categorical-data/ 

Winners solutions and approach: Xtreme ML Hack, AV DataFest 2017
https://www.analyticsvidhya.com/blog/2017/04/winners-solution-codes-xtreme-mlhack-datafest-2017/

https://stackoverflow.com/questions/32319831/how-to-preprocess-high-cardinality-categorical-features

https://datascience.stackexchange.com/questions/10509/how-to-deal-with-categorical-feature-of-very-high-cardinality
https://nbviewer.jupyter.org/github/esafak/mca/blob/master/docs/mca-BurgundiesExample.ipynb  MCA是标签型数据的PCA，不适用于我们的high cardinality问题 优先级拉低
https://github.com/esafak/mca 
       
学习重点：工程应用而不是理论，优先看代码（python,R)



技术圈>津南数字制造算法挑战赛【赛场一】决赛答辩
https://tianchi.aliyun.com/course/video?spm=5176.12586971.1001.7.32941048GSzXA2&liveId=41002
44:38 流程化的特征工程

自相关颜色图
https://tryolabs.com/blog/2017/03/16/pandas-seaborn-a-guide-to-handle-visualize-data-elegantly/


stacking
https://www.kaggle.com/arthurtok/introduction-to-ensembling-stacking-in-python

做比赛

看K-lab里的代码片段

整理之前看别人的比赛记录

待学习技术：
博弈论https://book.douban.com/subject/5346017/


------------------------本科统计学 培训计划------------------------
书：实用多元统计分析https://book.douban.com/subject/3519805/
属性数据分析https://book.douban.com/subject/30389931/
------------------------本科统计学 培训计划------------------------

（视频）：量化交易（主要看时间序列）https://www.bilibili.com/video/av15134256/?p=15
P13,P15

（视频）：SPSS统计分析从入门到精通
https://www.bilibili.com/video/av25302655?from=search&seid=6280014503625477752
spss统计分析与数据挖掘 (ppt+source_code)
第五章

(书）feature engineering for machine learning: principles and techniques for data scientists

（视频）：加州大学伯克利分校：心理学中的数据分析用统计数据进行假设检验http://open.163.com/movie/2017/6/8/1/MCM2FK2B1_MCMK6KV81.html
P11
（视频）：加州大学伯克利分校：公共健康-数据统计分析http://open.163.com/special/sp/statisticalanalysisofcategoricaldata.html

书：微星：时间序列分析的工程应用http://img.sslibrary.com/n/slib/book/slib/11883245/9ef0757f8b2546ab956a6e20c7e520d7/1a9282d275cca07033f28517f09f44ad.shtml?dxbaoku=false&deptid=1312&fav=http%3A%2F%2Fwww.sslibrary.com%2Freader%2Fpdg%2Fpdgreader%3Fd%3D277d7ca1ee38b3859bdc63fd681316b6%26ssid%3D11883245&fenlei=130113010601&spage=1&t=5&username=115.213.231.236&view=-1



Box-Cox 变换

有意思的网站：NASA：check for news and update :https://data.giss.nasa.gov/gistemp/
工具书的使用方法：工程用不到的话不看
工具书：R语言实战
工具书：R in a Nutshell（主要看外部包和统计检测方法）https://book.douban.com/subject/10438325/
https://zhuanlan.zhihu.com/p/26444240 技术一览

https://www.coursera.org/specializations/aml
课程首页

博弈论与经济行为https://book.douban.com/subject/1263734/
书：金融时间序列
数据挖掘与R语言（可以看一下第五章）https://book.douban.com/subject/24153573/


-----------------------------------------已经完成---------------------------------------------------------------------------


https://stackoverflow.com/questions/45235992/what-are-levels-in-a-pandas-dataframe

1. 看sklearn.importantce （看不了，目前数据集不完整）
2. train表中的time数据的转换 1002
isweekend? isweekday? ismorning? isafternoon? isnight? ismiddlenight?
                      5:00-11:00  11:00-17:00 17:00-23:00 23:00-5:00
3.更进一步： 统计 用户 在morning,afternoon,night,midnight购物的比例 1004
4. 计算用户最喜欢的商品的类型，最喜欢的商铺 1005
#   0.1.如果对用户购买商品的种类的众数进行特征构建，单个用户可能买了若干种类的商品，如何处理？
#   考虑那些众数为1个的用户，构建他们的favorite商品类型，对于其他用户用缺失代替,但对于标签数据的缺失值怎么处理？
#   （尝试去看lightgbm的标签数据缺失填充方法 没得）
#    (现在用用户最后一次购买商品的种类来填充

# 1.提取出所有曝光的记录，然后按广告排序，考虑统计曝光量的策略√
# 1.1 只提取曝光的记录，看是否有 同广告id 对应多个不同设置的情况，考虑该情况√
# 2. 绘制exposure与各inf中的数据的二维散点图，考虑其相关性√
# 2.1 对quality_ecpm和total_ecpm进行统计√
# 2.1.1考虑0值怎么办 ：直接剔除√
# 2.1.2 统计完之后需要对数据进行验证：找具体数据验证√
# 2.2 进行绘图： 以上两项和曝光量√
# 3.对未曝光的数据也要计算-相应的各项数√
# 4.根据report进行特征工程
# 4.1 考虑进行对exposure和unexposure的标准化处理
# 5.尝试用ARMA模型，代入历史留存这个变量，来解释数据据
# 5.1 探索历史留存，尝试用ARMA模型去描绘这个历史留存的变量

【机器学习】菜菜的sklearn课堂03 - 数据预处理和特征工程https://www.bilibili.com/video/av36467376?from=search&seid=5912966439620419291√

（视频）：应用时间序列分析https://www.bilibili.com/video/av41302125?from=search&seid=14220949878226996017√
（视频）：时序指数平滑 https://www.bilibili.com/video/av38756571?from=search&seid=11379537948141797463√
（书）：应用时间序列分析:看协整√
（书）：eviews统计分析与应用:只看eviews的实际操作√
eviews做时序的纯随机检验（白噪声检验）√
去学习很重要的时序技术：指数平滑√
时间序列分析——截尾和拖尾https://www.jianshu.com/p/f9e4cfc69e12√
很棒的时间序列视频https://www.bilibili.com/video/av29905215?from=search&seid=11379537948141797463√


冠军:嗯嗯 特征最重要 决定上限
# 误差产生点1  考虑统计quality_ecpm和total_ecpm的策略：若直接用均值，可能会造成误差 目前没有什么想法，只能先剔除0值后取均值
