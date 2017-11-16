import pandas as pd
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt
data=pd.read_csv('Match.csv')
killer = data[['Win_Type','Season_Id']]
a=[]
b=[]
for i in range(1,10):
    innone=killer.loc[killer['Season_Id'] == i]
    a.append(int(i))
    b.append(float(len(innone[innone['Win_Type']=='by wickets'])))

#print(a)
#print(b)


#print(b)
a=np.reshape(a,(len(a),1))
#print(a)
svr_lin= SVR(kernel= 'rbf', gamma=0.1)
svr_lin.fit(a,b)
plt.scatter(a,b,color='black',label='Data')
plt.plot(a,svr_lin.predict(a),color='green',label='prediction')
plt.show()
