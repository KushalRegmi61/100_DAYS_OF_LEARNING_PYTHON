import requests
import os

from dotenv import load_dotenv

load_dotenv()

# Getting hold of API environment variable
SHEET_API_KEY = os.getenv('SHEET_API_KEY')
SHEET_ENDPOINT = f"https://api.sheety.co/{SHEET_API_KEY}/flightDeals/prices"
SHEET_AUTHOIRZATION_HEADER=os.getenv('SHEET_AUTHOIRZATION_HEADER')
HEADERS = {
            "Authorization": SHEET_AUTHOIRZATION_HEADER,
            "Content-Type": "application/json"
        }

class DataManager:
    def __init__(self):
        self.destination_data = None


#TODO METHOD TO GET DATA FROM GOOGLE SHEET
    def get_data(self):
        response = requests.get(SHEET_ENDPOINT, headers=HEADERS)
        response.raise_for_status()  # Raise an exception for HTTP errors
        self.destination_data =response.json()['prices']
        return self.destination_data

#TODO METHOD TO UPDATE/EDIT A ROW IN GOOGLE SHEET
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEET_ENDPOINT}/{city['id']}",
                json=new_data,
                headers= HEADERS
            )
            

