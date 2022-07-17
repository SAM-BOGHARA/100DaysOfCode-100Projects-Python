from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.common.exceptions import NoSuchElementException , ElementClickInterceptedException
import time

FB_EMAIL = "shubhamboghara444@gmail.com"
FB_PASSWORD = "1234shubham1234"
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
options = webdriver.ChromeOptions()

options.binary_location = brave_path

chrome_driver_path = "C:/Program Files (x86)/DEVELOPMENT/chromedriver.exe"

s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s , options = options)
driver.maximize_window()
driver.get(url = "https://tinder.com")

main_window = driver.current_window_handle
time.sleep(10)
i_accept_x_path = '//*[@id="c1200009088"]/div/div[2]/div/div/div[1]/div[1]/button'
accept_button = driver.find_element(by = By.XPATH, value = i_accept_x_path)
accept_button.click()

time.sleep(4)
# //*[@id="c1200009088"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/span
login_x_path = '//*[@id="c1200009088"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/span'
login_button = driver.find_element(by = By.XPATH, value = login_x_path)
login_button.click()
time.sleep(10)

try:
    more_options_x_path = '//*[@id="c-528371988"]/div/div/div[1]/div/div/div[3]/span/button'
    more_options_button = driver.find_element(by = By.XPATH, value = more_options_x_path)
    more_options_button.click()
    time.sleep(10)
   
except NoSuchElementException:
    pass

time.sleep(8)
try:
    facebook_x_path = '//*[@id="c-528371988"]/div/div/div[1]/div/div/div[3]/span/div[2]/button/span[2]'
    facebook_login_button = driver.find_element(by = By.XPATH, value = facebook_x_path)
    facebook_login_button.click()
except NoSuchElementException:
    recovery_cancel = driver.find_element(by = By.XPATH, value = '//*[@id="u672211310"]/div/div/div[2]/button' ).click()
    login_x_path = '//*[@id="u-1894374910"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/span'
    login_button = driver.find_element(by = By.XPATH, value = login_x_path)
    login_button.click()

    facebook_x_path = '//*[@id="u672211310"]/div/div/div[1]/div/div/div[3]/span/div[2]/button/span[2]'
    facebook_login_button = driver.find_element(by = By.XPATH, value = facebook_x_path)
    facebook_login_button.click()
    time.sleep(5)
except Exception:
    facebook_x_path = '//*[@id="u672211310"]/div/div/div[1]/div/div/div[3]/span/div[2]/button/span[2]'
    facebook_login_button = driver.find_element(by = By.XPATH, value = facebook_x_path)
    facebook_login_button.click()
    

time.sleep(8)

for tab in driver.window_handles: 
    if tab != main_window:
        driver.switch_to.window(tab)
        print(driver.title)

time.sleep(8)


email_button = driver.find_element(by = By.XPATH, value = '//*[@id="email"]')
email_button.send_keys(FB_EMAIL)
pass_button = driver.find_element(by = By.XPATH, value = '//*[@id="pass"]')
pass_button.send_keys(FB_PASSWORD)
pass_button.send_keys(Keys.ENTER)

# driver.switch_to.window(main_window)
driver._switch_to.window( main_window)
time.sleep(10)

print(driver.title)

allow_button = driver.find_element(by = By.XPATH, value = '//*[@id="c-528371988"]/div/div/div/div/div[3]/button[1]/span').click()
time.sleep(2)
not_interested = driver.find_element(by = By.XPATH, value ='//*[@id="c-528371988"]/div/div/div/div/div[3]/button[2]/span').click()
time.sleep(15)

love_button = driver.find_element(by = By.XPATH, value ='//*[@id="c1200009088"]/div/div[1]/div/div/main/div/div/div[1]/div/div[4]/div/div[4]/button/span/span')
for i in range(15):
    try:
        love_button.click()
    except ElementClickInterceptedException:
        pass
    except NoSuchElementException:
        pass
    finally:
        love_button.click()
        time.sleep(10)


actions = ActionChains(driver)

for i in range(10):
    try:
        actions.send_keys(Keys.ARROW_RIGHT)
    except Exception:
        pass
    try:
        match = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a").click()
    except Exception:
        pass
    try:
        win_app = driver.find_element(By.XPATH, '//*[@id="u672211310"]/div/div/div[2]/button[2]').click()
    except Exception:
        pass

    time.sleep(6)
