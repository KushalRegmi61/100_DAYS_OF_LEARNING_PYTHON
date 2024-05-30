import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

today = datetime.now()

parameters = {
    "query": input("Enter the exercise you performed:"),
    "gender": "MALE",
    "weight_kg": "65",
    "height_cm": "165",
    "age": "19"
}
SHEET_AUTHORIZATION_KEY=os.getenv('SHEET_AUTHORIZATION_KEY')
#loading api id and api key from .env file
API_ENDPOINT= "https://trackapi.nutritionix.com/v2/natural/exercise"
API_ID= os.getenv('NUTRITIONIX_API_ID')
API_KEY= os.getenv('NUTRITIONIX_API_KEY')
SHEET_API_KEY=os.getenv('SHEET_API_KEY')
SHEET_ENDPOINT=f"https://api.sheety.co/{SHEET_API_KEY}/workoutTracking/workouts"

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

response = requests.post(API_ENDPOINT, headers=headers, json=parameters)

try:
    data = response.json().get('exercises', [])  # Get exercises or empty list if not found
    # print(data)
except requests.exceptions.JSONDecodeError:
    print("Response content is not in JSON format")
    print(response.text)

new_row_data = [{
    "workout": {
        "date": today.strftime('%Y/%m/%d'),
        "time": today.strftime('%X'),
        "exercise": exercise['name'].title(),
        "duration": exercise['duration_min'],
        "calories": exercise['nf_calories']
    }
} for exercise in data]

headers = {"Authorization": SHEET_AUTHORIZATION_KEY}
if new_row_data:  # Check if there is data to add
    for row_data in new_row_data:
        sheety_response = requests.post(SHEET_ENDPOINT, json=row_data,headers=headers)
    print(sheety_response.text)
else:
    print("No exercise data found.")
