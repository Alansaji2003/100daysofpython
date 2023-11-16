import smtplib
import datetime as dt
import random

my_email = "rockstaralansaji@gmail.com"
password = "xxxxxx"
file = open("quotes.txt")
quotes_list = file.readlines()
random_num = random.randint(0,len(quotes_list))

now = dt.datetime.now()
week = now.weekday()

print(week)
if week == 0:
    connection = smtplib.SMTP_SSL("smtp.gmail.com", 465)

    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="rockstaralansaji@gmail.com", msg=f"Subject:Your Monday Quote\n\n {quotes_list[random_num]}")
    connection.close()


