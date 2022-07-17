from selenium import webdriver

driver_path = "C:/Program Files (x86)/DEVELOPMENT/chromedriver.exe"
# brave_path = "C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe"

# option = webdriver.ChromeOptions()
# option.binary_location = brave_path
# option.add_argument("--incognito") OPTIONAL
# option.add_argument("--headless") OPTIONAL

# Create new Instance of Chrome
browser = webdriver.Chrome(executable_path="C:/chromedriver/chromedriver.exe")
# browser = webdriver.Chrome(driver_path)
PRODUCT_URL = "https://www.amazon.com/Acer-A515-56-50RS-i5-1135G7-Graphics-Fingerprint/dp/B08PG4W932/ref=sr_1_5?crid=1HIYXEEZ9G5HL&keywords=Acer+Aspire+5&qid=1649736411&sprefix=acer+aspire+5+%2Caps%2C525&sr=8-5"

browser.get(PRODUCT_URL)

# price = browser.find_elements_by_xpath('//*[@id="corePrice_desktop"]/div/table/tbody/tr[2]/td[2]/span[1]/span[2]')
# print(price)
# browser.close()
browser.quit()