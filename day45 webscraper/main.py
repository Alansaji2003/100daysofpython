from bs4 import BeautifulSoup
import lxml
import smtplib
from config import Config
config = Config()
my_email = "mailalantest@gmail.com"
password = config.Password

import requests
response = requests.get("https://news.ycombinator.com/news")
# print(response.text)  # we get the html
yc_web = response.text

soup = BeautifulSoup(yc_web, "html.parser")

# print(soup.find(name="a", rel="noreferrer").string) #printing the first article heading
article = soup.findAll(name="a", rel="noreferrer")

article_link = []
article_text = []
article_upvote = []
for x in article:

    article_link.append(x.get("href"))
    article_text.append(x.getText())
article_upvote = [int(score.getText().split()[0]) for score in soup.findAll(name="span", class_="score")]

large = 0
largest_index = 0
for x in article_upvote:
    if x > large:
        large = x
        largest_index = article_upvote.index(x)
#we can use max(article_upvote) to get the largest number in list
#printing the article with the largest index
message = f"The most Upvoted article of today is '{article_text[largest_index]}' which has total of  {article_upvote[largest_index]}  points. Link: {article_link[largest_index]}"
print(message)
#you can send yourself mail about this everyday if yu want
connection = smtplib.SMTP_SSL("smtp.gmail.com", 465)

connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="rockstaralansaji@gmail.com",msg=f"Subject:Todays news\n\n{message}")
connection.close()



# with open("website.html",encoding="utf-8") as file:
#     content = file.read()
#
#
# soup = BeautifulSoup(content, "html.parser") #you can use lxml if html doesnt work
# print(soup.title) #to get title tag
# print(soup.title.name) #to get tag name
# print(soup.title.string) #to get title string
# print(soup) #print the html
#
#
# print(soup.prettify()) #to get html wwith indentation
# print(soup.a) #print the first anchor tag in our website works with li,p etc
#
# all_anchor_tags = soup.findAll(name="a") #search and give all achor tags in the html
# print(all_anchor_tags)
#
# #we can do this with any tag names
# for tag in all_anchor_tags:
#     print(tag.string) #we can use the getText() method
#     print(tag.get("href"))
# #we can also use find all methood with attribute
# #for class we use class_
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
#
# #we can use selectors to search
# company_url = soup.select_one(selector="p a")
#
# print(company_url)
# #we can use that with id and class
# name = soup.select_one(selector="#name")
# print(name)
#
# #to select all items with class
# heading = soup.select(selector=".heading")
# print(heading)
#
#
