# tianchi-CBE

## 特征工程

### EDA
- EDA.ipynb

### 基础特征
[特征下载链接](https://pan.baidu.com/s/1dnVy2BmcEWLei_G7_A0PZw)（提取码：4tkz）

   - **base_feature.py **
      - flag = 1为训练集；flag = 2为测试集
      
   - **query_feature.py（点击类特征）**
      - 之前之后购买商品的次数
      - 之前之后购买相同商品的次数
      - 之前之后购买相同商品的次数
      - 之前之后购买相同店铺的次数
      - 之前之后购买相同类别的次数
      - 之前之后购买其他商品的次数　
      - 之前之后购买不同商品的种类（不重复）
      - 之前之后购买不同店铺的种类（不重复）
      - 之前之后购买不同种类的种类（不重复）

   - **leak_feature.py（购买间隔类特征）**
      - 购买时间间隔统计数据（最大值;最小值;中位数;平均数）
      - 第一次/最后一次购买和当前相距时间
      - 最近上一次下一次购买和当前相距时间
      - 之前之后购买次数所占的比例
      - 之前之后购买商品（不重复）所占的比例
      - 之前之后购买商铺（不重复）所占的比例
      - 之前之后购买商品种类（不重复）所占的比例
      
   - **compare_feature.py（竞争类特征）**
      - 之前之后购买低价商品（不重复）的个数
      - 之前之后购买高价商品（不重复）的个数
      - 之前之后购买低价商品种类（不重复）的个数
      - 之前之后购买高价商品种类（不重复）的个数
      - 之前之后购买低价商品店铺（不重复）的个数
      - 之前之后购买高价商品店铺（不重复）的个数
