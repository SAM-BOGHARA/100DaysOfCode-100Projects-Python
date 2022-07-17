import requests
from datetime import datetime
# from requests.auth import HTTPBasicAuth

GENDER = "male"
WEIGHT_KG = 72
HEIGHT_CM = 182
AGE = 19


API_KEY = "d45bb58f6eda3cc0aee09945af153538"
APPLICATION_ID = "946490c0"

NUTRITIONIX_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_URL = "https://api.sheety.co/ff15b376e1a0c55e0a79aa6315c39ab9/workoutTracking/workouts"
SHEETY_USERNAME = "ShubhamBoghara"
SHEETY_PASSWORD = "shubham,444"
# TOKEN = "gfhhghhdrsjuk"
TOKEN = "U2h1YmhhbUJvZ2hhcmE6c2h1YmhhbSw0NDQ="
input_text = input("Tell me which exercise you did? \n")

headers = {
    "x-app-id": APPLICATION_ID,
    "x-app-key": API_KEY
}

parameters = {
    "query": input_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=NUTRITIONIX_URL, json=parameters, headers=headers)

result = response.json()
print(result)


# google sheet working
today_date = datetime.now().strftime("%d%m%Y")
now_time = datetime.now().strftime("%X")

bearer_headers = {
    "Authorization": f"Basic {TOKEN}"
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
            
        }
    }

    bearer_headers = {
        "Authorization": f"Bearer {TOKEN}"
    }

    sheet_response = requests.post(SHEET_URL,
                                   json=sheet_inputs,
                                   auth=(SHEETY_USERNAME, SHEETY_PASSWORD),
                                   headers=bearer_headers)
    #    headers = bearer_headers)
    print(sheet_response.status_code)
    print(sheet_response.text)
