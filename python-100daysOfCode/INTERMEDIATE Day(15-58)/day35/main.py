import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv, find_dotenv
# from twilio.http.http_client import TwilioHttpClient

load_dotenv(find_dotenv())
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
api_key = os.getenv('OPEN_API_KEY')

parameters = {
    "lat": 19.243421,
    "lon": 72.855658,
    "exclude": "current,minutely,daily",
    "appid": api_key
}
response = requests.get(
    "https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
whether_data = response.json()
# print(whether_data["hourly"][0]["weather"][0]["id"])
weather_slice = whether_data["hourly"][:12]

will_rain = False


for hour_data in weather_slice:
    condition_code = (hour_data["weather"][0]["id"])

    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    # proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    # client = Client(account_sid, auth_token,http_client=proxy_client)
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body="It is going to rain today,Shubham.Dont forget to take the umbrella☔☔☔",
            from_='+16815252177',
            to='+919137943747'
        )

    print(message.status)
