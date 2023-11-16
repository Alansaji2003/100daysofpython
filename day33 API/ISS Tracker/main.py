import requests
import datetime as dt
import smtplib
import time

from requests.structures import CaseInsensitiveDict



my_email = "mailalantest@gmail.com"
password = "YOURPASSWORD"
MY_LAT = 12.9717248
MY_LONG = 77.5704728

def isOverHead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()

    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])
    url = f"https://api.geoapify.com/v1/geocode/reverse?lat={iss_latitude}&lon={iss_longitude}&apiKey=f4266527e4144e478fcbe66cc5c0c528"

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"

    resp = requests.get(url, headers=headers)
    location_data = resp.json()
    address = location_data["features"][0]["properties"]["formatted"]




    print("The iss is at",iss_latitude,iss_longitude,",",address,"\n")
    # to check whether the Space station is near +/-5 degree to my location
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True



def isNight():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = dt.datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    print("loading...\n")
    time.sleep(2)
    if isOverHead() and isNight():
        connection = smtplib.SMTP_SSL("smtp.gmail.com", 465)

        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="rockstaralansaji@gmail.com",
                            msg="Subject: Look UP👆\n\n The international space station is above you!")
        connection.close()


