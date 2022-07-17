from selenium import webdriver

driver_path = "C:/Program Files (x86)/DEVELOPMENT/chromedriver.exe"

# Create new Instance of Chrome
browser = webdriver.Chrome(executable_path="C:/chromedriver/chromedriver.exe")
PRODUCT_URL = "https://www.python.org/"

browser.get(PRODUCT_URL)

events_times = browser.find_elements_by_css_selector(".event-widget time")
events_names = browser.find_elements_by_css_selector(".event-widget li a")

events = {}

for n in range(len(events_times)):
    events[n] = {
        "time": events_times[n].text,
        "name": events_names[n].text,
    }

print(events)

browser.quit()