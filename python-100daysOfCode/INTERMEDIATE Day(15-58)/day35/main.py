import requests
import os
from twilio.rest import Client
# from twilio.http.http_client import TwilioHttpClient


account_sid = "AC67eeda91a29e6b8225e765a5def4e10b"
auth_token = "2278fd43fbaa1fe35439631c60370766"

api_key = "2a0c9cea278749498aca92edc221456b"
parameters = {
    "lat": -2.529450,
    "lon": -44.296951,
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
