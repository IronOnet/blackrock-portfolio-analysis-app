import requests
import json
from datetime import timedelta
from datetime import date



def one_day_stats (company, date):

	portfolioAnalysisRequest = requests.get("https://www.blackrock.com/tools/hackathon/performance", params= {'identifiers': company, 'startDate' : date, 'endDate' : date})
	
	dic_data = json.loads(portfolioAnalysisRequest.text) # string json 
	
	b = dic_data['resultMap']['RETURNS'][0] # enter data for the 

	
	for a in b:
		if (a == "latestPerf"):
			return b[a]['oneDay']



def one_week_stats (company, curr_date):
	output = 1
	for i in range(7):
		output *= (1 + one_day_stats(company, time_decrement(curr_date, i)))
	return output - 1

def time_decrement(time, i):
	time = int(time)
	delta = timedelta(days=-i)
	day = time % 100
	time//=100
	month = time%100
	time//=100
	year = time
	return time_convert((date(year,month,day) + delta))


def time_convert(date):
	return str((date.year*10000) + (date.month*100) + (date.day))



#one_day_stats("GS", '20161212')
today = date.today()
yesterday = date.today()
print(one_week_stats('GS',time_convert(today)))