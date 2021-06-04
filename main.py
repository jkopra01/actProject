import requests
from bs4 import BeautifulSoup
import pandas as pd

fromDate = '2021-01-13' #season start date
toDate = '2021-04-13'
fromSeason = '20202021'
toSeason = '20202021'

url = "https://www.naturalstattrick.com/teamtable.php?fromseason=20202021&thruseason=20202021&stype=2&sit=5v5&score=all&rate=n&team=all&loc=B&gpf=410&fd=" + fromDate + "&td=" + toDate + "#"

df = pd.read_html(url, header=0, index_col = 0, na_values=["-"])[0]

print(df)
file_name = "test1.csv"
df.to_csv(file_name, sep='\t', encoding='utf-8')