from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver_path = "C:/Program Files (x86)/DEVELOPMENT/chromedriver.exe"
browser = webdriver.Chrome(executable_path="C:/chromedriver/chromedriver.exe")
PRODUCT_URL = "https://en.wikipedia.org/wiki/Main_Page"

browser.get(PRODUCT_URL)
# 1
# number = browser.find_element_by_xpath('//*[@id="articlecount"]/a[1]')
# 2
# number = browser.find_element_by_id("articlecount")
# 3
# number = browser.find_element_by_css_selector("#articlecount a")
# number = browser.find_element(By.CSS_SELECTOR,"#articlecount a")
# print(number.text)

# all_portals = browser.find_element(by=By.LINK_TEXT, value="encyclopedia")
# all_portals.click()

search  = browser.find_element(by = By.NAME, value="search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)