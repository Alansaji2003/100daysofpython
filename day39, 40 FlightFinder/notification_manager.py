from twilio.rest import Client
import smtplib
import requests
my_email = "your gmail"
password = "your app password"
response = requests.get("your sheety endpoint")
class NotificationManager:
    def __init__(self):
        self.account_sid = "your twillio sid"
        self.auth_token = 'your auth token'

        self.client = Client(self.account_sid, self.auth_token)
    def send_SMS(self, price, origin, desti, from_, to, origin_city, desti_city):
        message = self.client.messages.create(
            body=f"Low Price Alert!! Only Rs.{price} to fly from {origin_city}({origin}) to {desti_city}({desti}), from {from_} to {to}",
            from_='your twilio number',
            to='your personal number'
        )

        print(message.status)
    def send_SMS_stopover(self, price, origin, desti, from_, to, origin_city, desti_city, stopover, viacity):
        message = self.client.messages.create(
            body=f"Low Price Alert!! Only Rs.{price} to fly from {origin_city}({origin}) to {desti_city}({desti}), from {from_} to {to}\n\nThe flight has stopover at {viacity}",
            from_='',
            to=''
        )
        print(message.status, "from stopover")
    def send_emails(self,price, origin, desti, from_, to, origin_city, desti_city):
        for users in response.json()["users"]:

            connection = smtplib.SMTP_SSL("smtp.gmail.com", 465)

            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=users["email"],
                                msg=f"Low Price Alert!! Only Rs.{price} to fly from {origin_city}({origin}) to {desti_city}({desti}), from {from_} to {to}")
            connection.close()
    def send_emails_stop(self,price, origin, desti, from_, to, origin_city, desti_city, stopover, viacity):
        for users in response.json()["users"]:

            connection = smtplib.SMTP_SSL("smtp.gmail.com", 465)

            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=users["email"],
                                msg=f"Subject:Message from Alan's Aviation Services!\n\nLow Price Alert!! Only Rs.{price} to fly from {origin_city}({origin}) to {desti_city}({desti}), from {from_} to {to}\n\nThe flight has stopover at {viacity}")
            connection.close()