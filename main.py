import requests
from datetime import datetime as dt
import os


NUTRITION_APP_ID = os.environ.get("NUTRITION_APP_ID")
NUTRITION_API_KEY = os.environ.get("NUTRITION_API_KEY")
EXERCISE_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
GENDER = "male"
WEIGHT_KG = 00.00 #Float
HEIGHT_CM = 00.00 #Float
AGE =  33 #INT
SHEETY_URL = "https://api.sheety.co/"



exercise_header = {
    "x-app-id": NUTRITION_APP_ID,
    "x-app-key": NUTRITION_API_KEY,
}

query = input("What exercise did you do? ")

exercise_params = {
    "query": query,
    "gender": GENDER,
    #"weight_kg:": WEIGHT_KG, for whatever reason getting an error message
    "height_cm": HEIGHT_CM,
    "age": AGE
}
nutrition_response = requests.post(url=EXERCISE_URL, json=exercise_params, headers=exercise_header)
data = nutrition_response.json()
date_time = dt.now()
todays_date = date_time.strftime("%d/%m/%Y")
hour_now = date_time.strftime("%X")

sheety_headers = {
    "Authorization": os.environ.get("sheety_token")
}

print(data)

for exersice in data["exercises"]:
    sheety_body = {
        "workout":
            {
                "date": todays_date,
                "time": hour_now,
                "exercise": exersice["name"],
                "duration": exersice["duration_min"],
                "calories": exersice["nf_calories"]

            }
    }
    #print(sheety_body)

    request = requests.post(url=SHEETY_URL, json=sheety_body, headers=sheety_headers)
    #print(request.text)
