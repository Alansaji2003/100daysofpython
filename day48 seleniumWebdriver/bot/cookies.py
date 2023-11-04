import time

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()

chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(3)
lang_en = driver.find_element(By.ID, value="langSelect-EN")
lang_en.click()
time.sleep(5)
cookie = driver.find_element(By.ID, value="bigCookie")

timeout = time.time() + 10
while True:

    cookie.click()

    if time.time() > timeout:

        cursor = driver.find_element(By.XPATH, value='//*[@id="product0"]')
        grandma = driver.find_element(By.XPATH, value='// *[ @ id = "product1"]')
        farm = driver.find_element(By.XPATH, value='//*[@id="product2"]')
        mine = driver.find_element(By.XPATH, value='//*[@id="product3"]')
        factory = driver.find_element(By.XPATH, value='//*[@id="product4"]')
        bank = driver.find_element(By.XPATH, value='//*[@id="product5"]')

        if cursor.get_attribute("class") == "product unlocked enabled" or grandma.get_attribute(
                "class") == "product unlocked enabled" or farm.get_attribute(
                "class") == "product unlocked enabled" or mine.get_attribute(
                "class") == "product unlocked enabled" or factory.get_attribute(
                "class") == "product unlocked enabled" or bank.get_attribute("class") == "product unlocked enabled":
            time.sleep(2)

            cursor_price = driver.find_element(By.XPATH, value='// *[ @ id = "productPrice0"]')
            grandma_price = driver.find_element(By.XPATH, value='// *[ @ id = "productPrice1"]')
            farm_price = driver.find_element(By.XPATH, value='// *[ @ id = "productPrice2"]')
            mine_price = driver.find_element(By.XPATH, value='// *[ @ id = "productPrice3"]')
            factory_price = driver.find_element(By.XPATH, value='// *[ @ id = "productPrice4"]')
            bank_price = driver.find_element(By.XPATH, value='// *[ @ id = "productPrice5"]')
            if bank_price.value_of_css_property("color") == "rgba(102, 255, 102, 1)":
                time.sleep(1)
                bank.click()
            elif factory_price.value_of_css_property("color") == "rgba(102, 255, 102, 1)":
                time.sleep(1)
                factory.click()
            elif mine_price.value_of_css_property("color") == "rgba(102, 255, 102, 1)":
                time.sleep(1)
                mine.click()
            elif farm_price.value_of_css_property("color") == "rgba(102, 255, 102, 1)":
                time.sleep(1)
                farm.click()
            elif grandma_price.value_of_css_property("color") == "rgba(102, 255, 102, 1)":
                time.sleep(1)
                grandma.click()
            else:
                time.sleep(1)
                cursor.click()

        timeout = timeout + 10
        continue
