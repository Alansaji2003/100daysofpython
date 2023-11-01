import smtplib
import requests
from bs4 import BeautifulSoup
import lxml
from config import Config
config = Config()
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9,ml;q=0.8",
        "Cookie": "PHPSESSID=b9ced46f1f89626c09777e26b0350b02; _ga=GA1.2.914121524.1698835683; _gid=GA1.2.553125194.1698835683; _ga_VL41109FEB=GS1.2.1698835683.1.0.1698835683.0.0.0"
    }

my_email = config.MY_EMAIL
password = config.MY_PASSWORD

response = requests.get("https://api.sheety.co/2685834fb03a94b5b5ace8da905168f4/amazonPrice/sheet1")

json_data = response.json()

print(json_data)

for users in json_data["sheet1"]:
    url = users["url"]

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")

    price = soup.find(name="span", class_="a-price-whole").getText().strip().replace(",","")
    formatted_price = price[0:len(price)-1]
    print(formatted_price)
    if float(formatted_price) <= float(users["price"]):

        connection = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=users["email"],
                        msg=f'Subject:Amazon Price Drop!!\n\nThe price has dropped for :{users["product"].encode("utf-8")}!!\n\n The current price is Rs: {formatted_price}!\n\n Grab that deal nigga!')
        connection.close()
    else:
        continue