from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import Config
config = Config()

FB_EMAIL = config.FACEBOOK_EMAIL
FB_PASSWORD = config.FACEBOOK_PASSWORD
PROXY = "IpOfTheProxy:PORT"

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--proxy-server=%s" % PROXY)
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("http://www.tinder.com")
driver.maximize_window()
sleep(2)
cookies = driver.find_element(By.XPATH, value='//*[@id="s-1837973528"]/div/div[2]/div/div/div[1]/div[1]/button')
cookies.click()
print("cookies accepted")
def login():
    sleep(2)
    login_button = driver.find_element(By.LINK_TEXT, value='Log in')
    login_button.click()
login()
print("login clicked")
sleep(10)
try:
    more_options = driver.find_element(By.XPATH, value='//*[@id="s728612692"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/button')
    more_options.click()
    print("more options clicked")
    sleep(10)
except:
    try:
        sleep(10)
        facebook = driver.find_element(By.XPATH,
                                       value='//*[@id="s728612692"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
        facebook.click()
        print("facebook clicked")
        sleep(10)
    except:
        sleep(5)
        close = driver.find_element(By.XPATH, value='//*[@id="s728612692"]/main/div/div[2]/button')
        close.click()
        login()
        sleep(5)
        facebook = driver.find_element(By.XPATH,
                                       value='//*[@id="s728612692"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
        facebook.click()
        print("facebook clicked")


else:
    try:
        close = driver.find_element(By.XPATH, value='//*[@id="s728612692"]/main/div/div[2]/button')
        close.click()
        login()
    except:
        pass
    sleep(10)
    facebook = driver.find_element(By.XPATH,
                                   value='//*[@id="s728612692"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
    facebook.click()
    print("facebook clicked")
sleep(10)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

email = driver.find_element(By.ID, value="email")
password = driver.find_element(By.ID, value="pass")

email.send_keys(FB_EMAIL)
password.send_keys(FB_PASSWORD)
password.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
print(driver.title)

sleep(20)
allow_location_button = driver.find_element(By.XPATH, value='//*[@id="s728612692"]/main/div/div/div/div[3]/button[1]')
allow_location_button.click()
try:
    alert = Alert(driver)
    alert.accept()
    driver.implicitly_wait(20)
except:
    pass
notifications_button = driver.find_element(By.XPATH, value='//*[@id="s728612692"]/main/div/div/div/div[3]/button[2]')
notifications_button.click()
try:
    alert = Alert(driver)
    alert.accept()
    driver.implicitly_wait(20)
except:
    pass


for n in range(15):
    sleep(30)
    try:
        print("called")
        wait = WebDriverWait(driver, 50)
        like_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="s-1837973528"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button'))).click()
        # print(like_button.text)
        # like_button.click()

    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            sleep(30)

driver.quit()








