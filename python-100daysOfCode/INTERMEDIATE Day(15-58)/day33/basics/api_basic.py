import requests

response = requests.get(url ="http://api.open-notify.org/iss-now.json")

print(response.status_code)
print(response._content)
print(response.cookies)
print(response.headers)
print(response.url)
data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)
print(iss_position)