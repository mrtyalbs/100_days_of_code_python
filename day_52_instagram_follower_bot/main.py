import time
from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

INSTAGRAM_LOGIN_URL = "https://www.instagram.com/accounts/login/"
EMAIL = "email@hotmail.com"
PASSWORD = "password"
SIMILAR_ACCOUNT = "python"
CHROME_DRIVER_PATH = "chromedriver.exe"

class InstaFollower:
    def __init__(self, driver_path):
        self.service = Service(CHROME_DRIVER_PATH)
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=self.service, options=self.options)

    def login(self):
        self.driver.get(INSTAGRAM_LOGIN_URL)
        time.sleep(1)

        username = self.driver.find_element(By.NAME, "username")
        password = self.driver.find_element(By.NAME, "password")

        username.send_keys(EMAIL)
        password.send_keys(PASSWORD, Keys.ENTER)
    def find_followers(self):
        time.sleep(2)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

        time.sleep(2)
        followers = self.driver.find_element(By.XPATH, "//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a")
        followers.click()

        time.sleep(2)
        modal = self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[2]")

        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")

        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/div[3]/button[2]")
                cancel_button.click()

instagram_bot = InstaFollower(CHROME_DRIVER_PATH)

instagram_bot.login()
instagram_bot.find_followers()
instagram_bot.follow()



