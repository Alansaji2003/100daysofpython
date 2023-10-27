
import requests
import os
from datetime import datetime, timedelta
from flight_search import FlightSearch
from data_manager import DataManager

from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "DEL"
flightsearch = FlightSearch()
notif = NotificationManager()

response = requests.get("your sheety endpoint")
sheet_data = response.json()

if sheet_data["prices"][0]["iataCode"] == "":
    print("Adding IATA codes to sheets.......")
    for entry in sheet_data["prices"]:
        city = entry["city"]
        res = flightsearch.get_flight_name(city)
        entry["iataCode"] = res

    datamanager = DataManager(sheet_data)

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data["prices"]:
    flight = flightsearch.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    try:
        if flight.stop_overs > 0:
            if flight.price < destination["lowestPrice"]:
                notif.send_SMS_stopover(flight.price, flight.origin_airport, flight.destination_airport, flight.out_date,
                               flight.return_date, flight.origin_city, flight.destination_city, flight.stop_overs, flight.via_city)
                notif.send_emails_stop(flight.price, flight.origin_airport, flight.destination_airport, flight.out_date,
                               flight.return_date, flight.origin_city, flight.destination_city, flight.stop_overs, flight.via_city)
            else:
                print("No good deals")
    except:
        continue
    try:
        if flight.price < destination["lowestPrice"]:
            print("SMS sending procedure...")
            notif.send_SMS(flight.price, flight.origin_airport, flight.destination_airport, flight.out_date, flight.return_date, flight.origin_city, flight.destination_city)
            notif.send_emails(flight.price, flight.origin_airport, flight.destination_airport, flight.out_date, flight.return_date, flight.origin_city, flight.destination_city)
    except:
        print("No discount Offers.")
