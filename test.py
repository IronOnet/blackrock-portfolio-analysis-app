import requests
import json

portfolioAnalysisRequest = requests.get("https://www.blackrock.com/tools/hackathon/performance", params= {'identifiers':"IXN"})
dic_data = json.loads(portfolioAnalysisRequest.text) #string json 

result = dic_data['resultMap'] # dictionary of dic_data

# below lines are to access the 0th item in the list and view its values, comment out if necessary
#values = result['RETURNS']
#dvalues = values[0]

#for i in dvalues:
	#print(i,':',dvalues[i])