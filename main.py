import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

SEASON_START_DATE_DAY_2019_2020 = 3
SEASON_START_DATE_MONTH_2019_2020 = 10
SEASON_END_DATE_DAY_2019_2020 = 12
SEASON_END_DATE_MONTH_2019_2020 = 3
SEASON_START_DATE_YEAR_2019_2020 = 2019
SEASON_END_DATE_YEAR_2019_2020 = 2020


seasonStartDate = '2021-01-13'
toDate = '2021-04-13'
fromDate = '2021-04-13'
fromSeason = '20202021'
toSeason = '20202021'

def getSeasonAndMerge(SD, SM, SY, ED, EM, EY):
    i = 0

    seasonStartDate = str(SY) + "-0" + str(SM) + "-0" + str(SD)
    fromSeason = str(SY)+str(EY)
    toSeason = fromSeason

    while not(SM == EM and SD == ED):
        if SD < 10:
            SD ='0'+str(SD)
        if SM < 10:
            SM = '0'+str(SD)
        toDate = str(SY) + "-" + str(SM) + "-" + str(SD)
        print(toDate)

        fromDate = toDate

       # print('start:'+str(SD) +"."+str(SM)+"."+str(SY)+" end:" + str(ED) +"."+str(EM)+"."+str(EY))
       # print (toDate)
       #Stop from overflowing the server
        time.sleep(1)
        statisticUrl = "https://www.naturalstattrick.com/teamtable.php?fromseason="+fromSeason+"&thruseason="+toSeason+"&stype=2&sit=5v5&score=all&rate=n&team=all&loc=B&gpf=410&fd=" + seasonStartDate + "&td=" + toDate + "#"
        dfStats = pd.read_html(statisticUrl, header=0, index_col = 0, na_values=["-"])[0]
        dfStats = dfStats.drop(columns=['GP', 'TOI','W','L','OTL','ROW','Points'])
        print(dfStats)
        i += 1

        SD = int(SD)
        SM = int(SM)
        if SD == 29 and SM == 2:
            SD = 1
            SM = 3
        if SD == 30 and SM == 4 or SM == 6 or SM == 9 or SM==11:
            SD=1
            SM +=1
        if SD == 31 and SM == 12:
            SD=1
            SM=1
            SY +=1
        if SD==31:
            SD=1
            SM+=1
        else:
            SD+=1
    print(i)




#statisticUrl = "https://www.naturalstattrick.com/teamtable.php?fromseason=20202021&thruseason=20202021&stype=2&sit=5v5&score=all&rate=n&team=all&loc=B&gpf=410&fd=" + seasonStartDate + "&td=" + toDate + "#"
resultsUrl = "https://www.naturalstattrick.com/teamtable.php?fromseason=20202021&thruseason=20202021&stype=2&sit=5v5&score=all&rate=n&team=all&loc=B&gpf=410&fd=" + fromDate + "&td=" + toDate

#dfStats = pd.read_html(statisticUrl, header=0, index_col = 0, na_values=["-"])[0]
#dfStats = dfStats.drop(columns=['GP', 'TOI','W','L','OTL','ROW','Points'])
dfResults = pd.read_html(resultsUrl, header=0, index_col = 0, na_values=["-"])[0]
dfResults = pd.DataFrame(dfResults, columns = ['Team', 'W'])
#print(dfStats)
print(dfResults)

file_name = "test1.csv"
#mergedDataFrames = dfStats.merge(dfResults, how = 'inner', on = ['Team'])
#mergedDataFrames.to_csv(file_name, sep='\t', encoding='utf-8')
#print(mergedDataFrames)

getSeasonAndMerge(SEASON_START_DATE_DAY_2019_2020,SEASON_START_DATE_MONTH_2019_2020,SEASON_START_DATE_YEAR_2019_2020,SEASON_END_DATE_DAY_2019_2020,SEASON_END_DATE_MONTH_2019_2020,SEASON_END_DATE_YEAR_2019_2020)

