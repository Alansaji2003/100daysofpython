##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
import datetime as dt
import random
import pandas
import smtplib

my_email = "mailalantest@gmail.com"
password = "avtmhpjaphjwghiv"
letter = ""
now = dt.datetime.now()
current_day = now.day
current_month = now.month
current_year = now.year


data = pandas.read_csv("birthdays.csv")

len = len(data)
for x in range(0,len):

    if data.iloc[x]["month"] == current_month:

        if data.iloc[x]["day"] == current_day:

            print("letter printing procedure")
            name = data.iloc[x]["name"]
            age = current_year - data.iloc[x]["year"]
            last = age%10
            if last == 1:
                th = "st"
            elif last == 2:
                th = "nd"
            elif last == 3:
                th = "rd"
            else:
                th = "th"

            num = random.randint(0,2)
            if num == 0:
                letter_file = open("letter_templates/letter_1.txt")
                letter_list = letter_file.readlines()
                letter_list[0] = f"Dear {name},\n"
            elif num == 1:
                letter_file = open("letter_templates/letter_2.txt")
                letter_list = letter_file.readlines()
                letter_list[0] = f"Dear {name},\n"
            elif num == 2:
                letter_file = open("letter_templates/letter_3.txt")
                letter_list = letter_file.readlines()
                letter_list[0] = f"Dear {name},\n"

            for i in letter_list:
                letter = letter + i





# 4. Send the letter generated in step 3 to that person's email address.

            connection = smtplib.SMTP_SSL("smtp.gmail.com", 465)

            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=data.iloc[x]["email"],
                                msg=f"Subject:HAPPY {age}{th} BIRTHDAY!!!!\n\n{letter}")
            connection.close()
