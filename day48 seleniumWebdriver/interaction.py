from selenium import webdriver
from selenium.webdriver.common.by import By
# for non alphabet/number keys
from selenium.webdriver.common.keys import Keys
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://chrome.google.com/webstore/detail/adblocker-for-youtube/ocpbafeegjjnfppckhackoojckloofan")
time.sleep(3)
add_to_chrome = driver.find_element(By.XPATH, value='/html/body/div[3]/div[2]/div/div/div[2]/div[2]/div')
add_to_chrome.click()
driver.get("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
# button = driver.find_element(By.CLASS_NAME, value="ytp-large-play-button")
# button.click()

# article_count = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')

# # to select the link or click
# article_count.click()

# # another way to click links is just by mentioning the link name

# view_source = driver.find_element(By.LINK_TEXT, value="View source")
# view_source.click()


# search_bar = driver.find_element(By.NAME, value="q")
# search_bar.send_keys("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

# Hitting enter key
# search_bar.send_keys(Keys.ENTER)
# videos = driver.find_element(By.LINK_TEXT, value="Videos")
# videos.click()
# link = driver.find_element(By.CLASS_NAME, value="qm9rMe")
# print(link.text)
# link.click()
