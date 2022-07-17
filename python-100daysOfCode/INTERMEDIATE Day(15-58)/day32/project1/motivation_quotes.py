import smtplib
import datetime as dt
import random as rd
import pandas as pd

MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD"
RECEIVER_EMAIL = "RECEIVERS EMAIL"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("INTERMEDIATE/day32/project1/quotes.txt", encoding="utf-8") as quote_file:
        all_quotes = quote_file.readlines()
        quote = rd.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        msg = f"Subject:Motivation QUOTES\n\n{quote}\nThis email is generated using python and You can trust Shubham..LOL."
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=RECEIVER_EMAIL,
                            msg=msg)
