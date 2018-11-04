import stocks
import news

data = news.companyCount(datetime.date.today(), 'google')

for element in data[1]: