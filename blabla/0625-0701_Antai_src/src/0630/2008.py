# 2008.py 进行sklearn的决策树建模
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
# criterion = "gini" (CART) or "entropy" (ID3)
# print (len(result)) 658786
# print (result.describe())
result = pd.read_csv("/home/kesci/work/2007.csv",encoding="utf-8")
result = result.dropna()

# print ("after-----------------------dropna")
# print (len(result)) 657262
# print (result.describe())
data_ = result[['fav_store','is_morning','is_afternoon','is_night', 'is_midnight', 'fav_cate','fav_store']]
target_ = result[['y_freq_i']]
X_train,X_test,y_train,y_test =train_test_split(data_,target_,test_size=0.2)
clf = DecisionTreeClassifier(criterion = 'entropy' ,random_state = 0)
clf.fit(X_train,y_train)
print ("clf. score")
print (clf.score(X_test, y_test))
print ("cv score")
print (cross_val_score(clf, X_test, y_test, cv=10))
# print (clf.score(X_test, y_test))
# print (clf.predict(X_test))
# clf.predict(X_test).to_csv("/home/kesci/work/baseline.csv")