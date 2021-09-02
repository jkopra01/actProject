import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

#2016-2017
SEASON_START_DATE_DAY_2016_2017 = 12
SEASON_START_DATE_MONTH_2016_2017 = 10
SEASON_END_DATE_DAY_2016_2017  = 9
SEASON_END_DATE_MONTH_2016_2017  = 4
SEASON_START_DATE_YEAR_2016_2017 = 2016
SEASON_END_DATE_YEAR_2016_2017 = 2017

#2017-2018
SEASON_START_DATE_DAY_2017_2018 = 4
SEASON_START_DATE_MONTH_2017_2018 = 10
SEASON_END_DATE_DAY_2017_2018  = 8
SEASON_END_DATE_MONTH_2017_2018  = 4
SEASON_START_DATE_YEAR_2017_2018  = 2017
SEASON_END_DATE_YEAR_2017_2018 = 2018

#2018-2019
SEASON_START_DATE_DAY_2018_2019 = 3
SEASON_START_DATE_MONTH_2018_2019 = 10
SEASON_END_DATE_DAY_2018_2019 = 6
SEASON_END_DATE_MONTH_2018_2019 = 4
SEASON_START_DATE_YEAR_2018_2019 = 2018
SEASON_END_DATE_YEAR_2018_2019 = 2019

#2019-2020
SEASON_START_DATE_DAY_2019_2020 = 3
SEASON_START_DATE_MONTH_2019_2020 = 10
SEASON_END_DATE_DAY_2019_2020 = 11
SEASON_END_DATE_MONTH_2019_2020 = 3
SEASON_START_DATE_YEAR_2019_2020 = 2019
SEASON_END_DATE_YEAR_2019_2020 = 2020

#Test dates
SEASON_START_DATE_DAY_TEST = 28
SEASON_START_DATE_MONTH_TEST = 12
SEASON_END_DATE_DAY_TEST = 3
SEASON_END_DATE_MONTH_TEST = 1
SEASON_START_DATE_YEAR_TEST = 2019
SEASON_END_DATE_YEAR_TEST = 2020

l = []
datesGathered = []

def getSeasonAndMerge(SD, SM, SY, ED, EM, EY):
    seasonStartDate = str(SY) + "-0" + str(SM) + "-0" + str(SD)
    fromSeason = str(SY)+str(EY)
    toSeason = fromSeason

    while not(SM == EM and SD == ED):
        if SD < 10:
            SD ='0'+str(SD)
        if SM < 10:
            SM = '0'+str(SM)
        toDate = str(SY) + "-" + str(SM) + "-" + str(SD)
        print(toDate)
        fromDate = toDate
        datesGathered.append(toDate)
       #Stop from overflowing the server
        time.sleep(10)
        statisticUrl = "https://www.naturalstattrick.com/teamtable.php?fromseason="+fromSeason+"&thruseason="+toSeason+"&stype=2&sit=5v5&score=all&rate=n&team=all&loc=B&gpf=410&fd=" + seasonStartDate + "&td=" + toDate + "#"
        dfStats = pd.read_html(statisticUrl, header=0, index_col = 0, na_values=["-"])[0]
        dfStats = dfStats.drop(columns=['GP', 'TOI','W','L','OTL','ROW','Points'])
        time.sleep(10)
        resultsUrl = "https://www.naturalstattrick.com/teamtable.php?fromseason="+fromSeason+"&thruseason="+toSeason+"&stype=2&sit=5v5&score=all&rate=n&team=all&loc=B&gpf=410&fd=" + fromDate + "&td=" + toDate
        dfResults = pd.read_html(resultsUrl, header=0, index_col = 0, na_values=["-"])[0]
        dfResults = pd.DataFrame(dfResults, columns = ['Team', 'W'])
        mergedDataFrames = dfStats.merge(dfResults, how = 'inner', on = ['Team'])
        l.append(mergedDataFrames)
        
        SD = int(SD)
        SM = int(SM)
        #february
        if SD == 29 and SM == 2:
            SD = 1
            SM = 3
        #months with 30 days
        elif (SD == 30 and SM == 4) or (SD == 30 and SM == 6) or (SD == 30 and SM == 9)  or (SD == 30 and SM == 11):
            SD=1
            SM +=1
        #end of year
        elif (SD == 31 and SM == 12):
            SD=1
            SM=1
            SY +=1
        #months with 31 days
        elif SD==31:
            SD=1
            SM+=1
        else:
            SD+=1

file_name = "nhlDataset1.csv"
getSeasonAndMerge(SEASON_START_DATE_DAY_2019_2020,SEASON_START_DATE_MONTH_2019_2020,SEASON_START_DATE_YEAR_2019_2020,SEASON_END_DATE_DAY_2019_2020,SEASON_END_DATE_MONTH_2019_2020,SEASON_END_DATE_YEAR_2019_2020)
getSeasonAndMerge(SEASON_START_DATE_DAY_2018_2019,SEASON_START_DATE_MONTH_2018_2019,SEASON_START_DATE_YEAR_2018_2019,SEASON_END_DATE_DAY_2018_2019,SEASON_END_DATE_MONTH_2018_2019,SEASON_END_DATE_YEAR_2018_2019)
getSeasonAndMerge(SEASON_START_DATE_DAY_2017_2018,SEASON_START_DATE_MONTH_2017_2018,SEASON_START_DATE_YEAR_2017_2018,SEASON_END_DATE_DAY_2017_2018,SEASON_END_DATE_MONTH_2017_2018,SEASON_END_DATE_YEAR_2017_2018)
getSeasonAndMerge(SEASON_START_DATE_DAY_2016_2017,SEASON_START_DATE_MONTH_2016_2017,SEASON_START_DATE_YEAR_2016_2017,SEASON_END_DATE_DAY_2016_2017,SEASON_END_DATE_MONTH_2016_2017,SEASON_END_DATE_YEAR_2016_2017)

pd.concat(l).to_csv(file_name, sep='\t', encoding='utf-8')



import unittest
import random
class TestNotebook(unittest.TestCase):
    def test_winColumnIsMerged(self):
        seasonData = getSeasonAndMerge(SEASON_START_DATE_DAY_TEST,SEASON_START_DATE_MONTH_TEST,SEASON_START_DATE_YEAR_TEST,SEASON_END_DATE_DAY_TEST,SEASON_END_DATE_MONTH_TEST,SEASON_END_DATE_YEAR_TEST)
        self.assertEqual(l[0].columns[l[0].columns.size-1], "W")    
            
    def test_dayMonthYearChangesCorrectly(self):
        seasonData = getSeasonAndMerge(SEASON_START_DATE_DAY_TEST,SEASON_START_DATE_MONTH_TEST,SEASON_START_DATE_YEAR_TEST,SEASON_END_DATE_DAY_TEST,SEASON_END_DATE_MONTH_TEST,SEASON_END_DATE_YEAR_TEST)
        self.assertIn("2020-01-01", datesGathered)

    def test_dataFromAllDatesIsCollected(self):
        dates = ["2019-12-28","2019-12-29","2019-12-30","2019-12-31","2020-01-01","2020-01-02"]
        seasonData = getSeasonAndMerge(SEASON_START_DATE_DAY_TEST,SEASON_START_DATE_MONTH_TEST,SEASON_START_DATE_YEAR_TEST,SEASON_END_DATE_DAY_TEST,SEASON_END_DATE_MONTH_TEST,SEASON_END_DATE_YEAR_TEST)
        self.assertIn(dates[random.randint(0, 5)], datesGathered) 
unittest.main(argv=[''], verbosity=2, exit=False)