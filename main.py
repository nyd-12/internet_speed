import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.keys import Keys

PROMISED_UP = 25
PROMISED_DOWN = 25
CHROME_DRIVER_PATH = r"C:\Development\chromedriver.exe"
TWITTER_EMAIL = os.environ.get('email')
TWITTER_PASSWORD = os.environ.get('password')
ISP = "JioCare"


class InternetSpeedTwitterBot:
    def __init__(self):
        options = ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=Service(executable_path=CHROME_DRIVER_PATH), options=options)
        self.up = 0
        self.down = 0
        self.get_internet_speed()

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(10)
        start_button = self.driver.find_element(By.CLASS_NAME, "start-button")
        start_button.click()
        time.sleep(60)
        self.down = float(self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div['
                                                             '3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div['
                                                             '1]/div/div[''2]/span').text)
        self.up = float(self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div['
                                                           '3]/div[''3]/div/div[3]/div/div/div[2]/div[1]/div['
                                                           '2]/div/div[2]/span').text)

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/home")
        self.driver.maximize_window()
        time.sleep(15)
        login_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div['
                                                          '2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div['
                                                          '2]/div/input')
        login_button.click()
        login_button.send_keys(TWITTER_EMAIL)
        time.sleep(2)
        login_button.send_keys(Keys.ENTER)
        time.sleep(2)
        password_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div['
                                                             '2]/div/div/div[2]/div[2]/div[1]/div/div/div['
                                                             '3]/div/label/div/div[2]/div[1]/input')
        password_button.click()
        password_button.send_keys(TWITTER_PASSWORD)
        time.sleep(8)
        password_button.send_keys(Keys.ENTER)
        time.sleep(8)
        tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div['
                                                          '2]/header/div/div/div/div[1]/div[3]/a')
        tweet_button.click()
        time.sleep(2)
        write_tweet = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
                                                         '2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div['
                                                         '2]/div/div/div/div/div/div/div['
                                                         '2]/div/div/div/div/label/div[1]/div/div/div/div/div/div['
                                                         '2]/div/div/div/div')
        write_tweet.click()
        write_tweet.send_keys(f"Hey @{ISP} why is my speed {bot.down}down/{bot.up}up when is was "
                              f"promised {PROMISED_DOWN}down/{PROMISED_UP}up!")
        time.sleep(4)
        # send_tweet = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div'
        #                                                 '/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div'
        #                                                 '/div/div[2]/div[4]/div/span/span')
        # send_tweet.click()


bot = InternetSpeedTwitterBot()
print(f"Up: {bot.up}")
print(f"Down: {bot.down}")
if bot.up < PROMISED_UP or bot.down < PROMISED_DOWN:
    bot.tweet_at_provider()
