## tianchi-CBE

## 特征工程

- **EDA**
	- EDA.ipynb

- **基础特征**
	- **query_feature.py**
      		- 之前之后购买商品的次数
      		- 之前之后购买相同商品的次数
      		- 之前之后购买相同商品的次数
      		- 之前之后购买相同店铺的次数
      		- 之前之后购买相同类别的次数
      		- 之前之后购买其他商品的次数　
      		- 之前之后购买不同商品的种类（不重复）
      		- 之前之后购买不同店铺的种类（不重复）
      		- 之前之后购买不同种类的种类（不重复）
      
	- 用户线上点击率
	- 用户线上购买率
	- 用户线上领取率
	- 用户线上不消费次数
	- 用户线上优惠券核销次数
	- 用户线上优惠券核销率
	- 用户线下不消费次数占线上线下总的不消费次数的比重
	- 用户线下的优惠券核销次数占线上线下总的优惠券核销次数的比重
	- 用户线下领取的记录数量占总的记录数量的比重
	
- **商家相关的特征**
	- 商家优惠券被领取次数
	- 商家优惠券被领取后不核销次数
	- 商家优惠券被领取后核销次数
	- 商家优惠券被领取后核销率
	- 商家优惠券核销的平均/最小/最大消费折率
	- 核销商家优惠券的不同用户数量，及其占领取不同的用户比重
	- 商家优惠券平均每个用户核销多少张
	- 商家被核销过的不同优惠券数量
	- 商家被核销过的不同优惠券数量占所有领取过的不同优惠券数量的比重
	- 商家平均每种优惠券核销多少张
	- 商家被核销优惠券的平均时间率
	- 商家被核销优惠券中的平均/最小/最大用户-商家距离

- **用户-商家交互特征**
	- 用户领取商家的优惠券次数
	- 用户领取商家的优惠券后不核销次数
	- 用户领取商家的优惠券后核销次数
	- 用户领取商家的优惠券后核销率
	- 用户对每个商家的不核销次数占用户总的不核销次数的比重
	- 用户对每个商家的优惠券核销次数占用户总的核销次数的比重
	- 用户对每个商家的不核销次数占商家总的不核销次数的比重
	- 用户对每个商家的优惠券核销次数占商家总的核销次数的比重

- **优惠券相关的特征**
	- 优惠券类型(直接优惠为0, 满减为1)
	- 优惠券折率
	- 满减优惠券的最低消费
	- 历史出现次数
	- 历史核销次数
	- 历史核销率
	- 历史核销时间率
	- 领取优惠券是一周的第几天
	- 领取优惠券是一月的第几天
	- 历史上用户领取该优惠券次数
	- 历史上用户消费该优惠券次数
	- 历史上用户对该优惠券的核销率

- **其它特征**
	
	这部分特征利用了赛题leakage，都是在预测区间提取的。
	- 用户领取的所有优惠券数目
	- 用户领取的特定优惠券数目
	- 用户此次之后/前领取的所有优惠券数目
	- 用户此次之后/前领取的特定优惠券数目
	- 用户上/下一次领取的时间间隔
	- 用户领取特定商家的优惠券数目
	- 用户领取的不同商家数目
	- 用户当天领取的优惠券数目
	- 用户当天领取的特定优惠券数目
	- 用户领取的所有优惠券种类数目
	- 商家被领取的优惠券数目
	- 商家被领取的特定优惠券数目
	- 商家被多少不同用户领取的数目
	- 商家发行的所有优惠券种类数目
