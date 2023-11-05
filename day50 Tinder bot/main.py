import time
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By




chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://tinder.com/app/recs")
driver.maximize_window()
print("website opened")
time.sleep(5)
accept_cookies = driver.find_element(By.XPATH, value='//*[@id="s-1837973528"]/div/div[2]/div/div/div[1]/div[1]/button')
accept_cookies.click()
print("cookies accepted")
def login():
    time.sleep(5)
    login = driver.find_element(By.LINK_TEXT, value='Log in')
    login.click()
    print("login clicked")
login()
time.sleep(5)
try:
    more_options = driver.find_element(By.XPATH, value='//*[@id="s728612692"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/button')
    more_options.click()
    print("more options clicked")
    time.sleep(5)
except:
    try:
        facebook = driver.find_element(By.XPATH,
                                       value='//*[@id="s728612692"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
        facebook.click()
        print("facebook clicked")
    except:
        time.sleep(5)
        close = driver.find_element(By.XPATH, value='//*[@id="s728612692"]/main/div/div[2]/button')
        close.click()
        login()
        time.sleep(5)
        facebook = driver.find_element(By.XPATH,
                                       value='//*[@id="s728612692"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
        facebook.click()
        print("facebook clicked")

else:
    try:
        facebook = driver.find_element(By.XPATH,
                                       value='//*[@id="s728612692"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
        facebook.click()
        print("facebook clicked")
    except:
        time.sleep(5)
        close = driver.find_element(By.XPATH, value='//*[@id="s728612692"]/main/div/div[2]/button')
        close.click()
        login()
        time.sleep(5)
        facebook = driver.find_element(By.XPATH,
                                       value='//*[@id="s728612692"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
        facebook.click()
        print("facebook clicked")
# //*[@id="s728612692"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/button
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print("Inside ",driver.title, " window")

facebook_email = driver.find_element(By.ID, value="email")
facebook_email.send_keys(FACEBOOK_EMAIL)
facebook_password = driver.find_element(By.ID, value="pass")
facebook_password.send_keys(FACEBOOK_PASSWORD)
print("email and password entered")

facebook_login = driver.find_element(By.XPATH, value='//*[@id="loginbutton"]')
facebook_login.click()
print("facebook login done")

driver.switch_to.window(base_window)
print("Inside ",driver.title, " window")
time.sleep(10)
#//*[@id="s728612692"]/main/div/div/div/div[3]/button[1]
#Allow location
try:
    allow_location_button = driver.find_element(By.XPATH,value='//*[@id="s728612692"]/main/div/div/div/div[3]/button[1]')
    allow_location_button.click()
    time.sleep(2)
    try:
        alert = Alert(driver)
        alert.accept()
        driver.implicitly_wait(20)
    except:
        pass
except:

    time.sleep(5)
    allow_location_button = driver.find_element(By.XPATH,
                                                value='//*[@id="s728612692"]/main/div/div/div/div[3]/button[1]')
    allow_location_button.click()
    time.sleep(2)
    try:
        alert = Alert(driver)
        alert.accept()
        driver.implicitly_wait(20)
    except:
        pass


#Disallow notifications
try:

    notifications_button = driver.find_element(By.XPATH, value='//*[@id="s728612692"]/main/div/div/div/div[3]/button[2]')
    notifications_button.click()
    try:
        alert = Alert(driver)
        alert.accept()
        driver.implicitly_wait(20)
    except:
        pass

except:
    time.sleep(5)
    notifications_button = driver.find_element(By.XPATH,
                                               value='//*[@id="s728612692"]/main/div/div/div/div[3]/button[2]')
    notifications_button.click()
    try:
        alert = Alert(driver)
        alert.accept()
        driver.implicitly_wait(20)
    except:
        pass
#swipe
while True:
    time.sleep(3)
    like = driver.find_element(By.XPATH, value='//*[@id="s-1837973528"]/div/div[1]/div/div/main/div/div/div[1]/div/div[3]/div/div[4]/button')