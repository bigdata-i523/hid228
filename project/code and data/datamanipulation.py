import pandas as pd
import operator
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt
import csv
teamDictionary={}
with open('Team.csv','r') as team:
    red=csv.DictReader(team)
    for d in red:
        teamDictionary.setdefault(int(d['Team_Id']),[]).append(d['Team_Name'])
print(teamDictionary)
lenOfDict=len(teamDictionary)
for i in range(1,lenOfDict+1):
    data = pd.read_csv('Match.csv')
    teamid=i
    #teamdata = data.loc[data['Team_Name_Id'] == 1 or data['Opponent_Team_Id'] == 1]

    teamdata = data.loc[operator.or_(data['Team_Name_Id'] == teamid,data['Opponent_Team_Id'] == teamid)]
    teamdatadf=teamdata[['Match_Id','Win_Type','Toss_Winner_Id','Team_Name_Id','Opponent_Team_Id','Match_Winner_Id','Toss_Decision']]
    matchids=teamdatadf['Match_Id'].tolist()

    teamdatadf.fillna(0)
    teamdatadf['wonmatch']=(teamdatadf['Match_Winner_Id']==teamid)
    wonmatch=teamdatadf['wonmatch'].tolist()
    print(len(matchids))
    scores=[]
    balldata=pd.read_csv('Ball_by_ball.csv')
    for value in matchids:
        matchdf=balldata.loc[operator.and_(balldata['Match_Id']==value,balldata['Team_Batting_Id']==teamid)]
        matchdf.fillna(0)
        score=matchdf['Batsman_Scored'].apply(pd.to_numeric, errors='coerce').sum()
        if(score<=100):
            scores.append("1")
        elif(score<=150):
            scores.append("2")
        elif(score<=200):
            scores.append("3")
        else:
            scores.append("4")
    print(len(scores))
    print(scores)

    teamdatadf=teamdatadf.fillna(0)
    teamdatadf['tossrole']=(teamdatadf['Toss_Winner_Id']==teamdatadf['Match_Winner_Id'])
    #print((teamdatadf['tossrole']))
    toss=teamdatadf['tossrole'].tolist()
    print(len(toss))
    # 1  -->Won toss batting first
    #2  --- > Won toss bowling first
    #3 --> Lost toss batting first
    #4 ---> lost toss bowling first

    teamdatadf['batting first']=operator.or_(operator.and_(teamdatadf['Toss_Winner_Id']==teamid,teamdatadf['Toss_Decision']=='bat'),operator.and_(teamdatadf['Toss_Winner_Id']!=teamid,teamdatadf['Toss_Decision']!='bat'))
    battingfirst=teamdatadf['batting first'].tolist()
    print(len(battingfirst))

    majorityscoredinboundaries=[]
    for value in matchids:
        matchdf=balldata.loc[operator.and_(balldata['Match_Id']==value,balldata['Team_Batting_Id']==teamid)]
        matchdf.fillna(0)
        score = matchdf['Batsman_Scored'].apply(pd.to_numeric, errors='coerce').sum()
        df4=matchdf[matchdf['Batsman_Scored'] == '4']
        df6=matchdf[matchdf['Batsman_Scored'] == '6']
        sum1=df4['Batsman_Scored'].apply(pd.to_numeric, errors='coerce').sum()
        sum2 =df6['Batsman_Scored'].apply(pd.to_numeric, errors='coerce').sum()
        sum=sum1+sum2
        if(sum>score-sum):
            majorityscoredinboundaries.append(True)
        else:
            majorityscoredinboundaries.append(False)
    print(majorityscoredinboundaries)
    print(len(majorityscoredinboundaries))

    finaldf=pd.DataFrame(data={"Match_ID":matchids,"BoundariesMajority":majorityscoredinboundaries,"Wontoss":toss,"BattingFirst":battingfirst,"scorerange":scores,"wonmatch":wonmatch})
    finaldf.to_csv(teamDictionary[teamid][0]+".csv",sep=',',index=False)
