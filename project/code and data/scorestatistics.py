import pandas as pd
import operator
import numpy as np
import matplotlib.pyplot as plt
import csv

teamDictionary={}
with open('Team.csv','r') as team:
    red=csv.DictReader(team)
    for d in red:
        teamDictionary.setdefault(int(d['Team_Id']),[]).append(d['Team_Name'])
print(teamDictionary)
lenOfDict=len(teamDictionary)
firstsCategory=[]
secondCategory=[]
thirdCategory=[]
fourthCategory=[]
teamList=[]
for i in range(1,lenOfDict+1):
    statsData=pd.read_csv(teamDictionary[i][0]+'.csv')
    listOfMatches=statsData['Match_ID'].tolist()
    totalMatches=len(listOfMatches)
    firstCategoryDF=statsData.loc[operator.and_(statsData['scorerange'] == 1, statsData['wonmatch'] == True)]
    secondCategoryDF = statsData.loc[operator.and_(statsData['scorerange'] == 2, statsData['wonmatch'] == True)]
    thirdCategoryDF = statsData.loc[operator.and_(statsData['scorerange'] == 3, statsData['wonmatch'] == True)]
    fourthCategoryDF = statsData.loc[operator.and_(statsData['scorerange'] == 4, statsData['wonmatch'] == True)]

    teamList.append(teamDictionary[i][0])
    firstsCategory.append((len(firstCategoryDF)/totalMatches)*100)
    secondCategory.append((len(secondCategoryDF)/totalMatches)*100)
    thirdCategory.append((len(thirdCategoryDF)/totalMatches)*100)
    fourthCategory.append((len(fourthCategoryDF)/totalMatches)*100)
print(len(teamList))
pos = list(range(len(thirdCategory)))
width = 0.2
fig, ax = plt.subplots(figsize=(20,10))
plt.bar(pos,
        #using df['pre_score'] data,
        firstsCategory,
        # of width
        width,
        # with alpha 0.5
        alpha=0.5,
        # with color
        color='#EE3224',
        # with label the first value in first_name
        label='firstsCategory')
plt.bar([p + width for p in pos],
        #using df['pre_score'] data,
        secondCategory,
        # of width
        width,
        # with alpha 0.5
        alpha=0.5,
        # with color
        color='#FFC222',
        # with label the first value in first_name
        label='secondCategory',align='center')
plt.bar([p + width*2 for p in pos],
        #using df['pre_score'] data,
        thirdCategory,
        # of width
        width,
        # with alpha 0.5
        alpha=0.5,
        # with color
        color='#F78F1E',
        # with label the first value in first_name
        label='thirdCategory',align='center')

plt.bar([p + width*3 for p in pos],
        #using df['pre_score'] data,
        fourthCategory,
        # of width
        width,
        # with alpha 0.5
        alpha=0.5,
        # with color
        color='green',
        # with label the first value in first_name
        label='fourthCategory',align='center')
plt.bar([p + width*3 for p in pos],
        #using df['pre_score'] data,
        [0,0,0,0,0,0,0,0,0,0,0,0,0],
        # of width
        width,
        # with alpha 0.5
        alpha=0.5,
        # with color
        color='black',
        # with label the first value in first_name
        label='nothing',align='center')
ax.set_ylabel('% matches won with scores')
ax.set_xticks([p + 1.5 * width for p in pos])
ax.set_xticklabels(teamList,rotation='vertical')
plt.xlim(min(pos)-width, max(pos)+width*6)
plt.legend(['Less than 100 and won the match', 'Scored > 100 & <150 and won the match', 'scored >150 and < 200 and won the match','Scored >200 and won the match'], loc='upper left')
plt.subplots_adjust(bottom=0.30)
plt.grid()
plt.savefig('scorestatictics.png')
plt.show()