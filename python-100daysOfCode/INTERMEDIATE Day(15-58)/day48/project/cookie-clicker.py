# from selenium import webdriver
# import time

# chrome_driver_path = "C:/Program Files (x86)/DEVELOPMENT/chromedriver.exe"
# driver = webdriver.Chrome(chrome_driver_path)
# driver.get("http://orteil.dashnet.org/experiments/cookie/")

# #Get cookie to click on.
# cookie = driver.find_element_by_id("cookie")

# #Get upgrade item ids.
# items = driver.find_elements_by_css_selector("#store div")
# item_ids = [item.get_attribute("id") for item in items]

# timeout = time.time() + 5
# five_min = time.time() + 60*5 # 5minutes

# while True:
#     cookie.click()

#     #Every 5 seconds:
#     if time.time() > timeout:

#         #Get all upgrade <b> tags
#         all_prices = driver.find_elements_by_css_selector("#store b")
#         item_prices = []

#         #Convert <b> text into an integer price.
#         for price in all_prices:
#             element_text = price.text
#             if element_text != "":
#                 cost = int(element_text.split("-")[1].strip().replace(",", ""))
#                 item_prices.append(cost)

#         #Create dictionary of store items and prices
#         cookie_upgrades = {}
#         for n in range(len(item_prices)):
#             cookie_upgrades[item_prices[n]] = item_ids[n]

#         #Get current cookie count
#         money_element = driver.find_element_by_id("money").text
#         if "," in money_element:
#             money_element = money_element.replace(",", "")
#         cookie_count = int(money_element)

#         #Find upgrades that we can currently afford
#         affordable_upgrades = {}
#         for cost, id in cookie_upgrades.items():
#             if cookie_count > cost:
#                  affordable_upgrades[cost] = id

#         #Purchase the most expensive affordable upgrade
#         highest_price_affordable_upgrade = max(affordable_upgrades)
#         print(highest_price_affordable_upgrade)
#         to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

#         driver.find_element_by_id(to_purchase_id).click()

#         #Add another 5 seconds until the next check
#         timeout = time.time() + 5

#     #After 5 minutes stop the bot and check the cookies per second count.
#     if time.time() > five_min:
#         cookie_per_s = driver.find_element_by_id("cps").text
#         print(cookie_per_s)
#         break

from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import StaleElementReferenceException

chrome_driver_path = "C:/Program Files (x86)/DEVELOPMENT/chromedriver.exe"
URL = "http://orteil.dashnet.org/experiments/cookie/"
PLAYTIME = 5

s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get(URL)


def update_costs():
    pr_dict = {product.split(" -")[0]: int(product.split(" - ")[1].replace(",", ""))
               for product in product_info if len(product) != 0}
    return pr_dict


def check_product():
    global product_dict
    cookies_num = int(driver.find_element(
        By.ID, "money").text.replace(",", ""))
    expensive_product = None
    for value, key in product_dict.items():
        if cookies_num > key:
            expensive_product = value
    if expensive_product is not None:
        try:
            buy_button = driver.find_element(By.ID, "store").find_element(
                By.CSS_SELECTOR, f"#buy{expensive_product}")
            buy_button.click()
            product_dict = update_costs()
        except StaleElementReferenceException as e:
            print(f"Exception found: {e}")
            pass


clicker = driver.find_element(By.ID, "cookie")
all_products = driver.find_elements(By.CLASS_NAME, "grayed")
product_info = [product.text.split("\n")[0] for product in all_products]
product_dict = update_costs()

timeout = datetime.now() + timedelta(minutes=PLAYTIME)

while datetime.now() < timeout:
    clicker.click()
    now_secs = int(datetime.now().strftime("%S"))
    if now_secs % 8 == 0:
        check_product()

speed = driver.find_element(By.ID, "cps").text
print(f"Cookies/second: {speed}")
driver.quit()
