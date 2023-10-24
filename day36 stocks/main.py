import requests
import os
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla"

#newsapi
news_url = "https://newsapi.org/v2/top-headlines"
news_params = {
    "q":COMPANY_NAME,
    "apiKey":"your apikey",
    "sources":"business-insider,business-insider-uk,techcrunch,next-big-future"
}
response = requests.get(news_url, params=news_params)
news_data = response.json()

#stockapi
stock_url = "https://www.alphavantage.co/query"
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": "your apikey"
}
stock_response = requests.get(stock_url, params=stock_params)
stock_data = stock_response.json()
daily = stock_data["Time Series (Daily)"]


#Twilioapi
account_sid = 'your api'
auth_token = 'your token'

client = Client(account_sid, auth_token)


open_value = []
for days in daily:
    open_value.append(daily[days]["1. open"])
day = float(open_value[0])
yesterday = float(open_value[1])
if day > yesterday :
    increase_perc = ((day - yesterday)/yesterday ) * 100
    if increase_perc > 3:
        message = client.messages.create(
            body=f'{STOCK} Stock: increased by {round(increase_perc, 2)}%\nHeadline: {news_data["articles"][0]["title"]}\nBrief: {news_data["articles"][0]["description"]}',
            from_='your from',
            to='your to'
        )

        print(message.status)
else:
    decrease_perc = ((yesterday - day)/yesterday ) * 100
    if decrease_perc > 3:
        message = client.messages.create(
            body=f'{STOCK} Stock: decreased by {round(decrease_perc, 2)}%\nHeadline: {news_data["articles"][0]["title"]}\nBrief: {news_data["articles"][0]["description"]}',
            from_='your from',
            to='your to'
        )


        print(message.status)







