import requests
from datetime import datetime
import os

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]
SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

query = {
    "query": input("Tell me what exercise you did? ")
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

response = requests.post(exercise_endpoint, headers=headers, json=query).json()

name_of_exercise = response["exercises"][0]["name"].title()
duration = response["exercises"][0]["duration_min"]
calories = response["exercises"][0]["nf_calories"]

date = datetime.now()

sheety_info = {
    "date": date.strftime("%d/%m/%Y"),
    "time": date.strftime("%X"),
    "exercise": name_of_exercise,
    "duration": duration,
    "calories": calories
}

body = {
    "workout": sheety_info
}

sheety_response = requests.post(SHEETY_ENDPOINT, json=body, auth=(USERNAME, PASSWORD))
