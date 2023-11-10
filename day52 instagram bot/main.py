import time

from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from config import Config
config = Config()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

USERNAME = config.USERNAME
PASSWORD = config.PASSWORD
SIMILAR = config.TARGET
class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/?hl=en")
        time.sleep(5)
        username = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        username.send_keys(USERNAME)
        password = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(PASSWORD)
        time.sleep(1)
        login = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button')
        login.click()
        time.sleep(5)
        try:
            save_info = self.driver.find_element(By.XPATH, value='//*[@id="mount_0_0_lm"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/section/div/button')
            save_info.click()
        except:
            time.sleep(5)
            print("Xpath didnt work for save_info")
            try:

                save_info = self.driver.find_element(By.CSS_SELECTOR,
                                                     value="div div div button")
                save_info.click()
            except:
                time.sleep(5)
                print("CSS didnt work")

                save_info = self.driver.find_element(By.CLASS_NAME,
                                                     value="._acan._acap._acas._aj1-._ap30")
                save_info.click()

        time.sleep(5)
        notif = self.driver.find_element(By.CSS_SELECTOR, value='.x7r02ix div div div button')
        print(notif.text)
        notif.click()
        time.sleep(5)






    def find_followers(self):
        try:
            search = self.driver.find_element(By.XPATH,
                                              value='//*[@id="mount_0_0_To"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span')
            search.click()
        except:
            print("xpath failed for search")
            search = self.driver.find_element(By.LINK_TEXT, value="Search")
            search.click()
            time.sleep(5)
            try:
                search_account = self.driver.find_element(By.XPATH, value='//*[@id="mount_0_0_Qi"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input')
                search_account.send_keys(SIMILAR)
            except:
                print("Xpath for search account didnt work")
                search_account = self.driver.find_element(By.CSS_SELECTOR,
                                                          value='.x5yr21d div div div input')
                search_account.send_keys(SIMILAR)
            time.sleep(2)
            try:
                account = self.driver.find_element(By.XPATH, value='//*[@id="mount_0_0_TQ"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/a')
                account.click()
            except:
                print("Xpath for account didnt work")
                account = self.driver.find_element(By.CSS_SELECTOR,
                                                   value='.x6s0dn4 div div a')
                account.click()
                time.sleep(5)
                followers = self.driver.find_element(By.CSS_SELECTOR, value=".x78zum5 li a")
                followers.click()
                time.sleep(5)
                time.sleep(5)
                scr1 = self.driver.find_element(By.XPATH,
                                                value='/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
                self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
                for i in range(10):
                    self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
                    time.sleep(2)

    def follow(self):
        while True:
            people = self.driver.find_elements(By.CSS_SELECTOR, value=".x1dm5mii div div div div div button")
            for each in people:
                print(each.text)
                time.sleep(5)
                try:
                    self.driver.execute_script("arguments[0].click();", each)
                except ElementClickInterceptedException:
                    cancel_button = self.driver.find_element(By.XPATH, value='/html/body/div[5]/div/div/div/div[3]/button[2]')
                    cancel_button.click()


# /html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]
# /html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]
# /html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]
# /html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]
# /html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]






bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()

