import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
import sklearn
import csv
from sklearn import datasets
from sklearn.ensemble import ExtraTreesClassifier, RandomForestClassifier
from sklearn.cross_validation import train_test_split
teamDictionary={}
with open('Team.csv','r') as team:
    red=csv.DictReader(team)
    for d in red:
        teamDictionary.setdefault(int(d['Team_Id']),[]).append(d['Team_Name'])
print(teamDictionary)
lenOfDict=len(teamDictionary)
for i in range(1,lenOfDict+1):
        csvname=teamDictionary[i][0]
        csvnamedotcsv=csvname+'.csv'
        data=pd.read_csv(csvnamedotcsv)

        predictors=data[['BattingFirst','BoundariesMajority','Wontoss','scorerange']]
        targets=data['wonmatch']
        data.dtypes
        data.describe()
        pred_train,pred_test,tar_train,tar_test=train_test_split(predictors,targets,test_size=0.4)
        pred_train.shape
        pred_test.shape
        tar_train.shape
        tar_test.shape

        classifier=RandomForestClassifier(n_estimators=50)
        classifier=classifier.fit(pred_train,tar_train)

        predictions=classifier.predict(pred_test)

        print(sklearn.metrics.accuracy_score(tar_test,predictions))
        print(sklearn.metrics.confusion_matrix(tar_test,predictions))


        model= ExtraTreesClassifier()
        model.fit(pred_train,tar_train)
        print(type(list(model.feature_importances_)))
        listToDf=list(model.feature_importances_)
        a=np.array(listToDf)
        print(listToDf)
        impacts=pd.DataFrame({'Team1':a})
        csv_input = pd.read_csv('impacts.csv')
        csv_input[csvname]=impacts['Team1']

        csv_input.to_csv('impacts.csv',index=False)
        print(impacts)
        trees=range(50)
        accuracy=np.zeros(50)
        for index in range(len(trees)):
                classifier=RandomForestClassifier(n_estimators=index+1)
                classifier.fit(pred_test,tar_test)
                predictions=classifier.predict(pred_test)
                accuracy[index]=sklearn.metrics.accuracy_score(tar_test,predictions)*100


        plt.plot(trees,accuracy,label=csvname)




plt.xlabel("Tree Number")
plt.ylabel("Accuracy")
plt.legend(loc='center left',bbox_to_anchor=(1, 0.5))
plt.title("Tree Number vs Accuracy")
plt.show()
plt.savefig('treenumvsaccuracy.png')