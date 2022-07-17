import datetime as dt
import smtplib

my_email = "YOUR EMAIL"
my_password = "YOUR PASSWORD"
receiver_email = "RECEIVERS EMAIL"

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email, to_addrs=receiver_email,
                        msg="Subject: CONGRATULATIONS\n\n Generated email by python code")
    connection.close()


now = dt.datetime.now()  # realtime
year = now.year
if year == 2022:
    print("2022")

print(now)

BIRTHDAY = dt.datetime(year=2022, month=11, day=13)
print(BIRTHDAY)
