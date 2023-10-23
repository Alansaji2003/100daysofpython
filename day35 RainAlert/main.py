import requests
import os
from twilio.rest import Client

#open weather credentials
OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast?"
api_key = "your api key"




# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID'] = 'your sid'
auth_token = os.environ['TWILIO_AUTH_TOKEN'] = 'your token'

client = Client(account_sid, auth_token)

weather_params = {
    "units":"metric",
    "cnt":4,
    "lat" : 8.5590445,
    "lon" : 76.9464702,
    "appid": api_key

}


response = requests.get(OWM_endpoint, params=weather_params)
data = response.json()
weather_list = data["list"]

rain = False

for dict in weather_list:
    if dict["weather"][0]["id"] < 700:
        rain = True

if rain:
    description = dict["weather"][0]["description"]
    message = client.messages.create(
        body=f"You might want to carry an umbrella ☔☔!!. There might be '{description}' in the next 12 hours.",
        from_='whatsapp:+14155238886',
        to='whatsapp:+918078255829'
    )
    print(message.status)