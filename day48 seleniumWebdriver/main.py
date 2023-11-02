from selenium import webdriver
from selenium.webdriver.common.by import By


# keep the Chrome window open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")
# different ways to get elements

# search = driver.find_element(By.NAME, value="query-builder-test")
# print(search.get_attribute("class"))
# price_rupees = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# print(price_rupees.text)
# driver.find_element(By.ID, value="query-builder-test")
# button = driver.find_element(By.NAME, value="button")
# print(button.size)
# link = driver.find_element(By.CSS_SELECTOR, value=".position-relative a")
# print(link.text)

# using xpath
# price = driver.find_element(By.XPATH, value='//*[@id="firstHeading"]/span')
# print(price.text)


# python.org exercise

event_dict = {}
date_list = []
event_list = []
date_objs = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
for date in date_objs:
    date_list.append(date.text)
event_objs = driver.find_elements(By.CSS_SELECTOR, value=".event-widget div ul a")
for event in event_objs:
    event_list.append(event.text)


for x in range(len(event_list)):
    event_dict[x] = {
        "time": date_list[x],
        "name": event_list[x]
    }

print(event_dict)


#to close browser
#close tab
# driver.close()
#close browser
driver.quit()
