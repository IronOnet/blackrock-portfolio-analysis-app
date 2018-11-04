from newsapi import NewsApiClient
import datetime
from stocks import get_stats, time_convert

# import pandas as pd
# data = pd.read_csv("companylist.csv")

def numArt(time, company):
    newsapi = NewsApiClient(api_key='3abb0cf162644ed9b7ed7d16ae649586')
    articles = newsapi.get_everything(q=company,from_param=str(time),to=str(time))
    return (articles['totalResults'])
    
dict = {
        'google':'GOOGL',
        'apple':'AAPL',
        'adobe':'ADBE',
        'applied materials':'AMAT',
        'amazon':'AMZN',
        'broadcom':'AVGO',
        'cisco':'CSCO',
        'citrix':'CTXS',
        'comcast':'CMCSA',
        'ebay':'EBAY',
        'expedia':'EXPE',
        'facebook':'FB',
        'intel':'INTC',
        'microsoft':'MSFT',
        'netflix':'NFLX',
        'nvidia':'NVDA',
        'paypal':'PYPL',
        'qualcomm':'QCOM',
        'starbucks':'SBUX',
        'tesla':'TSLA'
}

def getCount(time, company):
    newsapi = NewsApiClient(api_key='69f7c79fd92140f19221a257ec5e980c')
    # companies = list(data['Symbol'])'
    return numArt(time, company)

def getData(time, company):
    countList = []
    statsList = []
    count = 0
    for i in range(18, 30, 1):
        countList.append(getCount(time+datetime.timedelta(days= -1*i), company))
        statsList.append(get_stats(dict[company], time_convert(time+(datetime.timedelta(days= -i + 7)))))
    return (countList, statsList)

