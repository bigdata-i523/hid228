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
teamList=[]
percentBattingFirst=[]
percentBoundariesMajority=[]
percentWontoss=[]
for i in range(1,lenOfDict+1):
    statsData=pd.read_csv(teamDictionary[i][0]+'.csv')
    listOfMatches=statsData['Match_ID'].tolist()
    totalMatches=len(listOfMatches)
    #print(totalMatches)
    BattingFirstDF=statsData.loc[operator.and_(statsData['BattingFirst'] == True,statsData['wonmatch'] == True)]
    BoundariesMajorityDF=statsData.loc[operator.and_(statsData['BoundariesMajority'] == True,statsData['wonmatch'] == True)]
    WontossDF=statsData.loc[operator.and_(statsData['Wontoss'] == True,statsData['wonmatch'] == True)]
   # print(len(BattingFirstDF))
    #print((len(BattingFirstDF)/totalMatches)*100)
    teamList.append(teamDictionary[i][0])
    percentBattingFirst.append((len(BattingFirstDF)/totalMatches)*100)
    percentBoundariesMajority.append((len(BoundariesMajorityDF)/totalMatches)*100)
    percentWontoss.append((len(WontossDF)/totalMatches)*100)
print(percentBattingFirst)
print(percentBoundariesMajority)
print(percentWontoss)
print(teamList)

pos = list(range(len(percentBoundariesMajority)))
width = 0.25
fig, ax = plt.subplots(figsize=(10,5))
plt.bar(pos,
        #using df['pre_score'] data,
        percentBoundariesMajority,
        # of width
        width,
        # with alpha 0.5
        alpha=0.5,
        # with color
        color='#EE3224',
        # with label the first value in first_name
        label='percentBoundariesMajority')
plt.bar([p + width for p in pos],
        #using df['pre_score'] data,
        percentBattingFirst,
        # of width
        width,
        # with alpha 0.5
        alpha=0.5,
        # with color
        color='#FFC222',
        # with label the first value in first_name
        label='percentBattingFirst')
plt.bar([p + width*2 for p in pos],
        #using df['pre_score'] data,
        percentWontoss,
        # of width
        width,
        # with alpha 0.5
        alpha=0.5,
        # with color
        color='#F78F1E',
        # with label the first value in first_name
        label='percentWontoss')

ax.set_ylabel('% matches won with each factor as true')
ax.set_xticks([p + 1.5 * width for p in pos])
ax.set_xticklabels(teamList,rotation='vertical')
plt.legend(['Majority runs in boundaries and won match', 'Batting First and Won Match', 'Won Toss and Won match'], loc='upper left')
plt.subplots_adjust(bottom=0.30)
plt.grid()
plt.savefig('otherstatistics.png')
plt.show()
