import requests
from datetime import datetime

TODAY = datetime.now()
USER_NAME = "xxx"
TOKEN = "xxx"
GRAPH_ID = "xxx"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService":"yes",
    "notMinor": "yes",


}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name":"MyCodingGraph",
    "unit":"min",
    "type": "float",
    "color": "sora"
}
headers = {

    "X-USER-TOKEN":TOKEN
}

# response = requests.post(url=graph_endpoint,json=graph_config, headers=headers)
# print(response.text)
update_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"
update_config = {
    "date": str(TODAY.strftime("%Y%m%d")), #to format the date as we want
    "quantity":input("Type today's total coding time in minutes.")
}
response = requests.post(url=update_endpoint, json=update_config, headers=headers)
print(response.text)

#delete request
#response = requests.delete(url=update_endpoint, json=update_config, headers=headers)