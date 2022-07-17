#https://docs.google.com/forms/d/e/1FAIpQLSeZKOiZmorn_YLDmp4QD9vmwxpUtz2NzxkWAZH3b55yk0K1lQ/viewform?usp=sf_link

from bs4 import BeautifulSoup as bs
import requests 
import lxml
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException , ElementClickInterceptedException

EMAIL = ''
PASSWORD = ''

# PRODUCT_URL = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-115.3519960625%2C%22east%22%3A-78.3500429375%2C%22south%22%3A16.11804716108558%2C%22north%22%3A55.471647063596215%7D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A4%7D"
PRODUCT_URL = "https://www.zillow.com/nd/rentals/1-_beds/1.0-_baths/?searchQueryState=%7B%22mapBounds%22%3A%7B%22west%22%3A-104.927508640625%2C%22east%22%3A-95.677020359375%2C%22south%22%3A43.039729471022326%2C%22north%22%3A51.59323319035313%7D%2C%22mapZoom%22%3A6%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22baths%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A37%2C%22regionType%22%3A2%7D%5D%2C%22usersSearchTerm%22%3A%22North%20Dakota%22%2C%22schoolId%22%3Anull%2C%22pagination%22%3A%7B%7D%7D"

add = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
price = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
linkk = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
submit = 'NPEfkd RveJvd snByac'

email = '//*[@id="identifierId"]'
password = '//*[@id="password"]/div[1]/div/div[1]/input'
HEADER = {
    "Accept-Language":"en-US,en;q=0.9",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.79 Safari/537.36"
}

response = requests.get(url = PRODUCT_URL,headers = HEADER)
content = response.text


soup = bs(content,"lxml")
address_list = []
price_tag_list = []
link_list = []


addresses = soup.find_all(class_ = "list-card-addr")
for tag in addresses:
    address_list.append(tag.getText())
print(address_list)

price = soup.find_all(class_ = "list-card-price")
for tag in price:
    price_tag_list.append(tag.getText().split("+")[0].replace("$",''))
print(price_tag_list)



link = soup.find_all(name = "a",class_ = "list-card-link list-card-link-top-margin")
for tag in link:
    l = tag.get("href")
    link_list.append(f"https://www.zillow.com{l}")
print(link_list)


brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
options = webdriver.ChromeOptions()

options.binary_location = brave_path

chrome_driver_path = "C:/Program Files (x86)/DEVELOPMENT/chromedriver.exe"

s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s , options = options)
driver.maximize_window()

driver.get('https://docs.google.com/forms/d/e/1FAIpQLSeZKOiZmorn_YLDmp4QD9vmwxpUtz2NzxkWAZH3b55yk0K1lQ/viewform?usp=sf_link')

time.sleep(2)
email_ = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,email))).send_keys(EMAIL)
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="identifierNext"]/div/button/span'))).click()
pass_ = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,password))).send_keys(PASSWORD)
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="passwordNext"]/div/button/span'))).click()
time.sleep(10)
for n in range(len(price_tag_list)):
    time.sleep(10)
    driver.get('https://docs.google.com/forms/d/e/1FAIpQLSeZKOiZmorn_YLDmp4QD9vmwxpUtz2NzxkWAZH3b55yk0K1lQ/viewform?usp=sf_link')
    
    address = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,add)))
    priceee = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,price)))
    linkkk =  WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,linkk)))
    submit = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')))
    address.send_keys(address_list[n])
    priceee.send_keys(price_tag_list[n])
    linkkk.send_keys(link_list[n])
    
    submit.click()
