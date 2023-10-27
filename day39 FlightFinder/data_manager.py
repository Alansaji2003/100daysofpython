import requests


class DataManager:
    def __init__(self, sheet_data):
        for entry in sheet_data["prices"]:
            id = entry["id"]
            update_config = {
                "price":{
                    "iataCode": entry["iataCode"]
                }
            }
            response = requests.put(url=f"your sheety endpoint{id}", json=update_config)

