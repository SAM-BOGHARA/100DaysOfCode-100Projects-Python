from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException , ElementClickInterceptedException


brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
options = webdriver.ChromeOptions()

options.binary_location = brave_path

chrome_driver_path = "C:/Program Files (x86)/DEVELOPMENT/chromedriver.exe"

s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s , options = options)
driver.maximize_window()
driver.get(url = "https://leetcode.com")
