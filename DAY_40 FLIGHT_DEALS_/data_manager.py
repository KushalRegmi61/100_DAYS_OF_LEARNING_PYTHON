import requests
import os

from dotenv import load_dotenv

load_dotenv()

# Getting hold of API environment variable
SHEET_API_KEY = os.getenv('SHEET_API_KEY')
SHEET_ENDPOINT = f"https://api.sheety.co/{SHEET_API_KEY}/flightDeals/prices"
SHEETY_DETAILS_ENDPOINT = f"https://api.sheety.co/{SHEET_API_KEY}/flightDeals/userDetails"

SHEET_AUTHORIZATION_HEADER=os.getenv('SHEET_AUTHORIZATION_HEADER')
HEADERS = {
            "Authorization": SHEET_AUTHORIZATION_HEADER,
            "Content-Type": "application/json"
        }

class DataManager:
    def __init__(self):
        self.destination_data = None


#TODO METHOD TO GET DATA FROM PRICE GOOGLE SHEET
    def get_data(self):
        response = requests.get(SHEET_ENDPOINT, headers=HEADERS)
        response.raise_for_status()  # Raise an exception for HTTP errors
        self.destination_data =response.json()['prices']
        return self.destination_data

#TODO METHOD TO GET USER_DETAILS FROM  USER DETAILS GOOGLE SHEET
    def user_details(self):
        response = requests.get(url=SHEETY_DETAILS_ENDPOINT,headers=HEADERS)
        response.raise_for_status()
        self.user_details = response()['userDetails']
        if response.status_code == '200':
            return self.user_details
        else:
            print(response.text)

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
            
    def insert_userDetails(self, firstName, lastName, email):
        try:
            new_user_data = {
                "userDetail": {
                    "firstName": firstName,
                    "lastName": lastName,
                    "email": email
                }
            }
            response = requests.post(
                url=SHEETY_DETAILS_ENDPOINT,
                headers=HEADERS,
                json=new_user_data
            )
        except requests.exceptions.HTTPError as err:
            pass
        except Exception as err:
            pass
        
    def get_user_data(self):
        try:
            response = requests.get(url=SHEETY_DETAILS_ENDPOINT, headers=HEADERS)
            response.raise_for_status()
            data = response.json()
            self.destination_data = data["userDetails"]
            return self.destination_data
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")
            return None
        except Exception as err:
            print(f"An error occurred: {err}")
            return None
            
