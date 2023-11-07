import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# KEEP CHROME BROWSER OPEN AFTER A PROGRAM FINISHES
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.amazon.com/Apple-MacBook-10-core-Storage-English/dp/B0C8GNPF42/ref=ex_alt_wg_d?_encoding=UTF8&pd_rd_i=B0C8GNFTJQ&pd_rd_w=nXSd5&pf_rd_p=4e1b46a8-daf9-4433-b97e-d6df97cf3699&pf_rd_r=AGX8NY92FJXPMKH1VPN6&pd_rd_wg=vaHr0&pd_rd_r=1595bdb6-a1af-43a5-8a7c-e5e5ad131351&content-id=amzn1.sym.4e1b46a8-daf9-4433-b97e-d6df97cf3699&th=1")
#driver.get("https://www.amazon.com/Apple-MacBook-10-core-Storage-English/dp/B0C8GNPF42/ref=ex_alt_wg_d?_encoding=UTF8&pd_rd_i=B0C8GNFTJQ&pd_rd_w=nXSd5&pf_rd_p=4e1b46a8-daf9-4433-b97e-d6df97cf3699&pf_rd_r=AGX8NY92FJXPMKH1VPN6&pd_rd_wg=vaHr0&pd_rd_r=1595bdb6-a1af-43a5-8a7c-e5e5ad131351&content-id=amzn1.sym.4e1b46a8-daf9-4433-b97e-d6df97cf3699&th=1")
# Find the element by class name
time.sleep(20)
price_dollar = driver.find_element(By.XPATH, value='//*[@id="corePrice_desktop"]/div/table/tbody/tr/td[2]/span[1]/span[2]')

# Get the text of the element
price_text = price_dollar.text
print(price_dollar)
print(f"The price is {price_text}")

# # Close the WebDriver
# driver.quit()