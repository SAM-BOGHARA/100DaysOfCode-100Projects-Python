from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException , ElementClickInterceptedException

USERNAME = 'python_bott11'
PASSWORD = 'shubham,444@.'
TARGET = 'nike'
class InstagramFollowerBot:
    
    def __init__(self):
        self.brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
        self.options = webdriver.ChromeOptions()

        self.options.binary_location = self.brave_path

        self.chrome_driver_path = "C:/Program Files (x86)/DEVELOPMENT/chromedriver.exe"

        self.s = Service(self.chrome_driver_path)
        self.driver = webdriver.Chrome(service=self.s , options = self.options)
        self.driver.maximize_window()
        self.driver.get("https://www.instagram.com/accounts/login/")

    
    def login(self):
        # time.sleep(10)
        username = WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')))
        username.send_keys(USERNAME)
        password = WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')))
        password.send_keys(PASSWORD)
        login = self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]').click()
        time.sleep(15)
        save_info = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/section/main/div/div/div/section/div/button').click()
        

    def find_follower(self):
        # not_now_notification = self.driver.find_element(By.XPATH,'//*[@id="mount_0_0_Bu"]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]').click()
        self.driver.get(f"https://www.instagram.com/{TARGET}/")
        time.sleep(15)
        followers = self.driver.find_element(By.XPATH,'//*[@id="mount_0_0_z3"]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[3]/a').click()

        time.sleep(5)
        modal = self.driver.find_element(By.XPATH,'//*[@id="mount_0_0_z3"]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight",modal)
            time.sleep(10)

    def follow(self):
        for i in range(100):
            try:
                follow_btn = self.driver.find_element(By.XPATH,'//*[@id="fc5b510bf9d84"]/button').click()
                time.sleep(10)
            except ElementClickInterceptedException:
                # cancel = self.driver.find_element(By.XPATH,'').click()
                continue
            except NoSuchElementException:
                continue
        

bot = InstagramFollowerBot()
bot.login()
time.sleep(5)
bot.find_follower()
time.sleep(2)
bot.follow()



