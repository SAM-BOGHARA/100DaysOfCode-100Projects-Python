from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver_path = "C:/Program Files (x86)/DEVELOPMENT/chromedriver.exe"

# Create new Instance of Chrome
browser = webdriver.Chrome(driver_path)
PRODUCT_URL = "https://secure-retreat-92358.herokuapp.com/"

browser.get(PRODUCT_URL)

fname = browser.find_element(by = By.NAME, value="fName")
fname.send_keys("Shubham")

lname = browser.find_element(by = By.NAME, value="lName")
lname.send_keys("Boghara")

email = browser.find_element(by = By.NAME, value="email")
email.send_keys("shubhamboghara444@gmail.com")

sign_up_button = browser.find_element(by = By.CSS_SELECTOR, value = "form button")

sign_up_button.click()


