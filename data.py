import requests
import json
from datetime import timedelta
from datetime import date


# Takes in company and date and returns the stats for one day
def one_day_stats (company, date):

	portfolioAnalysisRequest = requests.get("https://www.blackrock.com/tools/hackathon/performance", params= {'identifiers': company, 'startDate' : date, 'endDate' : date})
	dic_data = json.loads(portfolioAnalysisRequest.text) # string json 
	b = dic_data['resultMap']['RETURNS'][0] # enter data for the 
	return b.get("latestPerf")['oneDay']


# Takes in company and date and returns the stats for one week
def one_week_stats (company, curr_date):
	output = 1
	for i in range(7):
		output *= (1 + one_day_stats(company, time_decrement(curr_date, i)))
	return output - 1

# Takes in API date format and number of days before and returns API date format
def time_decrement(time, i):
	time = int(time)
	delta = timedelta(days=-i)
	day = time % 100
	time//=100
	month = time%100
	time//=100
	year = time
	return time_convert((date(year,month,day) + delta))

# Converts from datetime date to API date form
def time_convert(date):
	return str((date.year*10000) + (date.month*100) + (date.day))

# Today's date
today = date.today()

# Main function to run, takes a company and optionally the date and returns the seven day stats
def get_stats(company,cdate=time_convert(today)):
	return ("%.3f" % one_week_stats(company,cdate))
	
