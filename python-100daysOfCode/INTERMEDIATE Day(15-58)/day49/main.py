import time
from selenium import * 
from selenium import webdriver
from selenium.webdriver.common import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException

ACCOUNT_EMAIL = "shubhamboghara444@student.sfit.ac.in"
ACCOUNT_PASSWORD = "shubham,444@."
chrome_driver_path = "C:/Program Files (x86)/DEVELOPMENT/chromedriver.exe"
URL = "https://www.linkedin.com/jobs/search/?f_AL=true&f_WT=2&geoId=102713980&keywords=python%20developer%20intern&location=India"
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get(URL)

sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()

time.sleep(10)

email_field = driver.find_element_by_id("username")
email_field.send_keys(ACCOUNT_EMAIL)

password_field = driver.find_element_by_id("password")
password_field.send_keys(ACCOUNT_PASSWORD)

password_field.send_keys(Keys.ENTER)


job_titles = driver.find_elements_by_css_selector(".job-card-container--clickable")

for title in job_titles:
    print(f"{title} called")
    title.click()
    time.sleep(2)
    try:
        apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply_button.click()
        time.sleep(5)

        phone = driver.find_element_by_class_name("fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys("9137943747")
        
        submit_button = driver.find_element_by_css_selector("footer button")
        if submit_button.get_attribute("data-control-name")  =="continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()

            time.sleep(2)

            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-diaalog-btn")[1]
            discard_button.click()
            print("skipped ,,complex")
            continue
        else:
            submit_button.click()

        time.sleep(2)

        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        print("No application,,skippped")
        continue

time.sleep(5)
driver.quit()