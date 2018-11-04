from newsapi import NewsApiClient
import datetime
from datetime import timedelta
from data import get_stats, time_convert

# import pandas as pd
# data = pd.read_csv("companylist.csv")

def numArt (time, company):
    newsapi = NewsApiClient(api_key='69f7c79fd92140f19221a257ec5e980c')
    articles = newsapi.get_everything(q=company,from_param=str(time),to=str(time))
    return (articles['totalResults'])
 



def companyCount(time, company):
    newsapi = NewsApiClient(api_key='69f7c79fd92140f19221a257ec5e980c')
    print()
    # companies = list(data['Symbol'])
    countList = []
    statsList = []
    count = 0
    for i in range(18, 28, 1):
        countList.append(numArt(time+datetime.timedelta(days= -1*i), company))
        statsList.append(get_stats(company, time_convert(time+(datetime.timedelta(days= -i + 7)))))
    return (countList, statsList)
print(companyCount(datetime.date.today(), 'GOOGL'))
