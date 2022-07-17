from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException , ElementClickInterceptedException

DOWN = 100 
UP = 12
TWITTER_EMAIL = "shubhamboghara444@student.sfit.ac.in"
TWITTER_PASSWORD = "shubh,444@."



class InternetSpeeedTwitterBot:
    
    def __init__(self):
        self.brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
        self.options = webdriver.ChromeOptions()

        self.options.binary_location = self.brave_path

        self.chrome_driver_path = "C:/Program Files (x86)/DEVELOPMENT/chromedriver.exe"

        self.s = Service(self.chrome_driver_path)
        self.driver = webdriver.Chrome(service=self.s , options = self.options)
        self.driver.maximize_window()

    

    # def get_internet_speed(self):
    #     self.driver.get("https://www.speedtest.net/")
    #     time.sleep(10)
    #     goo_button = self.driver.find_element(By.CSS_SELECTOR,".start-button a").click()
    #     time.sleep(100)
    #     download_speed = self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
    #     print(download_speed)

    #     upload_speed = self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
    #     print(upload_speed)


    def tweet(self):

        self.driver.get(url = "https://twitter.com") 
        time.sleep(10)
        # login = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div[2]/div/div/div/div/div[2]/div/div[1]/a/div/span/span').click()

        # sign_in_with_google  = self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[2]/span[1]').click()


        sign_in = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div/span/span').click()
        time.sleep(15)
        username = self.driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input').send_keys(TWITTER_EMAIL)
        time.sleep(15)
        next_step = self.driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span').click()
        time.sleep(15)
        password = self.driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys(TWITTER_PASSWORD)
        time.sleep(15)
        login_button = self.driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/span/span').click()

        time.sleep(15)
        try:
            tweet = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div/svg/g/path').click()
        except NoSuchElementException:
            tweet2 = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div/svg').click()

bot = InternetSpeeedTwitterBot()
# bot.get_internet_speed()
bot.tweet()