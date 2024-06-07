import requests
import os
from pprint import pprint
from dotenv import load_dotenv
from datetime import datetime, timedelta

# Load environment variables from .env file
load_dotenv()

class FlightSearch:
    def __init__(self):
        self.api_key = os.getenv('AMADEUS_API_KEY')
        self.api_secret = os.getenv('AMADEUS_API_SECRET')
        self.token = self.get_token()
        self.departure_date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
        self.return_date = (datetime.now() + timedelta(days=180)).strftime("%Y-%m-%d")

    def iata_code(self, cityname):
        CITY_SEARCH_URL = "https://test.api.amadeus.com/v1/reference-data/locations"
        
        params = {
            "keyword": cityname,
            "subType": "CITY"
        }

        headers = {
            "Authorization": f"Bearer {self.token}"
        }

        response = requests.get(CITY_SEARCH_URL, headers=headers, params=params)
        if response.status_code == 200:
            city_info = response.json()
            try:
                code = city_info["data"][0]['iataCode']
            except (IndexError, KeyError):
                return None
                
            return code
        
        else:
            return None

    def get_token(self):
        TOKEN_URL = "https://test.api.amadeus.com/v1/security/oauth2/token"

        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        data = {
            "grant_type": "client_credentials",
            "client_id": self.api_key,
            "client_secret": self.api_secret
        }

        try:
            response = requests.post(TOKEN_URL, headers=headers, data=data)
            response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)

            token = response.json().get('access_token')
            if not token:
                raise Exception("Failed to retrieve access token.")
            return token
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def fetch_flight_data(self, departure, destination):
        url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        params = {
            "originLocationCode": departure,
            "destinationLocationCode": destination,
            "departureDate": self.departure_date,
            "returnDate": self.return_date,
            "adults": 1,
            "nonStop": 'true',  # Corrected to lowercase 'true'
            "max": 10,
            "currencyCode": "GBP"
        }

        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching flight data: {response.status_code}")
            return None