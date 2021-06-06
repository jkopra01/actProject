import requests
from bs4 import BeautifulSoup
import pandas as pd

seasonStartDate = '2021-01-13'
toDate = '2021-04-13'
fromDate = '2021-04-13'
fromSeason = '20202021'
toSeason = '20202021'

statisticUrl = "https://www.naturalstattrick.com/teamtable.php?fromseason=20202021&thruseason=20202021&stype=2&sit=5v5&score=all&rate=n&team=all&loc=B&gpf=410&fd=" + seasonStartDate + "&td=" + toDate + "#"
resultsUrl = "https://www.naturalstattrick.com/teamtable.php?fromseason=20202021&thruseason=20202021&stype=2&sit=5v5&score=all&rate=n&team=all&loc=B&gpf=410&fd=" + fromDate + "&td=" + toDate

dfStats = pd.read_html(statisticUrl, header=0, index_col = 0, na_values=["-"])[0]
dfResults = pd.read_html(resultsUrl, header=0, index_col = 0, na_values=["-"])[0]
dfResults = pd.DataFrame(dfResults, columns = ['Team', 'W'])
print(dfStats)
print(dfResults)



file_name = "test1.csv"
dfStats.to_csv(file_name, sep='\t', encoding='utf-8')


