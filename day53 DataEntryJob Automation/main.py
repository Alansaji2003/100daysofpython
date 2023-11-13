import time

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

url = []
address = []
price = []

response = requests.get(f"https://appbrewery.github.io/Zillow-Clone/")
print(response.status_code)

soup = BeautifulSoup(response.text, "html.parser")
address_tags = soup.findAll(name="address")
for ad in address_tags:
    address.append(ad.text.replace("\n", "")[32:-30].replace("|", ","))
price_tags = soup.findAll(name="span", class_="PropertyCardWrapper__StyledPriceLine")
for pri in price_tags:
    price.append(pri.text[0:6])
for a in soup.findAll('a', href=True, class_="StyledPropertyCardDataArea-anchor"):
    url.append(a['href'])

for x in range(len(address)):
    time.sleep(1)
    driver.get("https://forms.gle/ULaPqr69emSyJcTH9")
    time.sleep(1)
    address_input = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_input.send_keys(address[x])
    price_input = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input.send_keys(price[x])
    url_input = driver.find_element(By.XPATH,
                                      value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    url_input.send_keys(url[x])
    submit_button = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit_button.click()
    time.sleep(3)