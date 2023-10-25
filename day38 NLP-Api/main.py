import requests
from datetime import datetime
import os
d = datetime.now()

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
endpoint = os.environ.get("ENDPOINT")
WEIGHT = 70
HEIGHT = 172
AGE = 20

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id":"0",
    "Content-Type": "application/json"
}


json_params = {
 "query":input("Tell me the exercise you did "),
 "gender":"male",
 "weight_kg":WEIGHT,
 "height_cm":HEIGHT,
 "age":AGE
}

response = requests.post(url=endpoint, json=json_params, headers=header)
exercise_json = response.json()

sheety_header = {
"Authorization": os.environ.get("AUTH")
}
sheety_endpoint = os.environ.get("SHEETY_ENDPOINT")


for exercise in exercise_json["exercises"]:

    sheet_inputs = {
        "workout": {
            "date": d.strftime("%d/%m/%Y"),
            "time": d.strftime("%I:%M %p"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    result = requests.post(url=sheety_endpoint, json=sheet_inputs, headers=sheety_header)
    print(result.text)



if result.status_code == 200:
    print("success! The entries are added to 'MY_WORKOUT' spreadsheet in google sheets")
