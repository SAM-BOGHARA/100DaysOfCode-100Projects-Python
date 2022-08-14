from bs4 import BeautifulSoup as bs
import requests 
import smtplib 
import lxml

MY_MAIL = "shubhamboghara444@gmail.com"
MY_PASSWORD = "shubhamb,444@"
PRODUCT_URL = "https://www.amazon.com/Acer-A515-56-50RS-i5-1135G7-Graphics-Fingerprint/dp/B08PG4W932/ref=sr_1_5?crid=1HIYXEEZ9G5HL&keywords=Acer+Aspire+5&qid=1649736411&sprefix=acer+aspire+5+%2Caps%2C525&sr=8-5"
HEADER = {
    "Accept-Language":"en-US,en;q=0.9",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.79 Safari/537.36"
}

my_bet = 600

response = requests.get(url = PRODUCT_URL,headers = HEADER)
content = response.text

# print(content)
# print(response.status_code)

soup = bs(content,"lxml")
price_tag_list = []
span_tag = soup.find_all("span",class_ = "a-offscreen")
title_tag = soup.find("span", id = "productTitle",class_ = "a-size-large product-title-word-break")

for tag in span_tag:
    price_tag_list.append(tag.getText())

title = title_tag.getText()
str_price = price_tag_list[1]

price_split = str_price.split("$")
the_price = float(price_split[1])
print(the_price)


if my_bet >= the_price:

    message = f"Subject:Amazon Price Alert!\n\nYour Favourite {title} is now available for \n\n{the_price} ,Grab it Buddy.\n\n{PRODUCT_URL}"

    with smtplib.SMTP("smtp.gmail.com",port = 587) as connection: 
        connection.starttls()
        result = connection.login(MY_MAIL,MY_PASSWORD)
        connection.sendmail(from_addr = MY_MAIL,
                            to_addrs = MY_MAIL,
                            msg = message)