from newsapi import NewsApiClient
import datetime
from data import get_stats, time_convert

# import pandas as pd
# data = pd.read_csv("companylist.csv")

def companyCount(time, company):
    newsapi = NewsApiClient(api_key='69f7c79fd92140f19221a257ec5e980c')

    # companies = list(data['Symbol'])
    countList = []
    statsList = []
    count = 0

    for i in range(0, 90, 3):
        articles = newsapi.get_everything(q=company,from_param=str(time+datetime.timedelta(days=i)),to=str(time+datetime.timedelta(days=i)))
        for j in articles:
            count+=1
        countList.append(count)
        statsList.append(get_stats(company, time_convert(time+(datetime.timedelta(days=i+7)))))
    return (countList, statsList)
print(companyCount(datetime.date.today() - (datetime.timedelta(days=30)), 'GOOGL'))
