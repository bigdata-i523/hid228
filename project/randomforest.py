import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
import sklearn
from sklearn import datasets
from sklearn.ensemble import ExtraTreesClassifier, RandomForestClassifier
from sklearn.cross_validation import train_test_split

data=pd.read_csv('teamstats1.csv')

predictors=data[['BattingFirst','BoundariesMajority','Wontoss','scorerange']]
targets=data['wonmatch']
data.dtypes
data.describe()
pred_train,pred_test,tar_train,tar_test=train_test_split(predictors,targets,test_size=0.4)
pred_train.shape
pred_test.shape
tar_train.shape
tar_test.shape

classifier=RandomForestClassifier(n_estimators=25)
classifier=classifier.fit(pred_train,tar_train)

predictions=classifier.predict(pred_test)

print(sklearn.metrics.accuracy_score(tar_test,predictions))
print(sklearn.metrics.confusion_matrix(tar_test,predictions))


model= ExtraTreesClassifier()
model.fit(pred_train,tar_train)
print(model.feature_importances_)
trees=range(25)
accuracy=np.zeros(25)
for index in range(len(trees)):
    classifier=RandomForestClassifier(n_estimators=index+1)
    classifier.fit(pred_test,tar_test)
    predictions=classifier.predict(pred_test)
    accuracy[index]=sklearn.metrics.accuracy_score(tar_test,predictions)

plt.cla()
plt.plot(trees,accuracy)
plt.show()