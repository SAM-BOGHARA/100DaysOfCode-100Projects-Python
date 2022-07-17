import requests
import smtplib
from datetime import *
import time
MY_LAT = 19.075983
MY_LONG = 72.877655
MY_EMAIL = "shubhamboghara444@gmail.com"
MY_PASSWORD = "shubham,444@."


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    data = response.json()
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_latitude <= MY_LONG+5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }
    response1 = requests.get(
        url="http://api.sunrise-sunset.org/json", params=parameters)
    response1.raise_for_status()
    data1 = response1.json()
    sunrise = int(data1["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data1["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        # it is dark
        return True


while True:
    # time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                            msg="Subject:ISS NOTIFIER EMAIL.\n\nLook up👆👆The ISS is above you in the sky.")


# if the ISS is close to my current position
# and it is currently dark
# then send me email to tell me to look up
# bonus : this code runs every 60 seconds on the cloud
