import requests
from flight_data import FlightData
class FlightSearch:
    def __init__(self):
        self.ENDPOINT = "your tequila kiwi endpoint"
        self.header = {
            "apikey":"your api key"
        }

    def get_flight_name(self, name):
        params = {
            "term":name,
            "locale":"in",
            "location_types": "airport",
            "limit":10,
            "active_only" : "true"
        }

        response = requests.get(url=f"{self.ENDPOINT}/locations/query", params=params, headers=self.header).json()

        iata = response["locations"][0]["id"]
        return iata

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):

        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",

            "max_stopovers": 0,
            "curr": "INR"
        }

        response = requests.get(
            url=f"{self.ENDPOINT}/v2/search",
            headers=self.header,
            params=query,
        )

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            print("Checking for stopover flights..")
            query2 = {
                "fly_from": origin_city_code,
                "fly_to": destination_city_code,
                "date_from": from_time.strftime("%d/%m/%Y"),
                "date_to": to_time.strftime("%d/%m/%Y"),
                "nights_in_dst_from": 7,
                "nights_in_dst_to": 28,
                "flight_type": "round",

                "max_stopovers": 2,
                "curr": "INR"
            }
            response = requests.get(
                url=f"{self.ENDPOINT}/v2/search",
                headers=self.header,
                params=query2,
            )
            try:
                data = response.json()["data"][0]
            except:
                print("no stopover")
                return None
            else:
                flight_data = FlightData(
                    price=data["price"],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][1]["cityTo"],
                    destination_airport=data["route"][1]["flyTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][2]["local_departure"].split("T")[0],
                    stop_overs=2,
                    via_city=data["route"][0]["cityTo"]
                )
                print(f"{flight_data.via_city}: Rs.{flight_data.price}")
                return flight_data

        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )
            print(f"{flight_data.destination_city}: Rs.{flight_data.price}")
            return flight_data

