import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta
from flight_search import FlightSearch
import time

class FlightData(FlightSearch):
    def __init__(self, price=None, departure_airport_code=None, destination_airport_code=None, departure_date=None, last_ticketing_date=None, airline_name=None, transit_city_location=None, transit_city_name=None):
        super().__init__()
        self.price = price
        self.departure_airport_code = departure_airport_code
        self.destination_airport_code = destination_airport_code
        self.departure_date = departure_date
        self.last_ticketing_date = last_ticketing_date
        self.airline_name = airline_name
        self.transit_city_location = transit_city_location
        self.transit_city_name = transit_city_name

    def __repr__(self):
        return (f"FlightData(price={self.price}, departure_airport_code={self.departure_airport_code}, "
                f"destination_airport_code={self.destination_airport_code}, departure_date={self.departure_date}, "
                f"return_date={self.last_ticketing_date}, airline_name={self.airline_name}, transit_city_location={self.transit_city_location}, "
                f"transit_city_name={self.transit_city_name})")

    def get_daily_cheapest_flight(self, flight_data):
        if flight_data is None or 'data' not in flight_data:
            return None

        if flight_data['data']:
            cheapest_offer = flight_data['data'][0]

            # Extract flight details from the cheapest offer
            itineraries = cheapest_offer.get("itineraries", [])
            if len(itineraries) < 2:
                return FlightData(price='N/A',
                                  departure_airport_code='N/A',
                                  destination_airport_code='N/A',
                                  departure_date='N/A',
                                  last_ticketing_date='N/A',
                                  airline_name='N/A',
                                  transit_city_location="N/A",
                                  transit_city_name="N/A"
                                  )

            departure_segment = itineraries[0].get("segments", [])[0]
            return_segment = itineraries[1].get("segments", [])[0]

            departure_airport_code = departure_segment.get("departure", {}).get("iataCode")
            destination_airport_code = return_segment.get("arrival", {}).get("iataCode")
            departure_date = departure_segment.get("departure", {}).get("at")
            last_ticketing_date = cheapest_offer.get("lastTicketingDate", "N/A")
            price = cheapest_offer.get("price", {}).get("total")

            # Extract airline name
            airline_code = departure_segment.get("carrierCode")
            airline_name = flight_data.get("dictionaries", {}).get("carriers", {}).get(airline_code)

            # Extract transit city location if it exists
            transit_city_location = None
            transit_city_name = None
            if len(itineraries[0].get("segments", [])) > 1:
                transit_city_location = itineraries[0]["segments"][1].get("departure", {}).get("iataCode")
                # Use an alternative API to get the city name for the transit location
                transit_city_name = self.get_city_name(transit_city_location)

            return FlightData(price=price,
                              departure_airport_code=departure_airport_code,
                              destination_airport_code=destination_airport_code,
                              departure_date=departure_date,
                              last_ticketing_date=last_ticketing_date,
                              airline_name=airline_name,
                              transit_city_location=transit_city_location,
                              transit_city_name=transit_city_name)
        return None

    def get_city_name(self, iata_code):
        # Example of using an alternative API (OpenStreetMap Geocode API) to get the city name
        url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat=0&lon=0&zoom=18&addressdetails=1&accept-language=en&city={iata_code}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            city_name = data.get("address", {}).get("city")
            return city_name
        return None

    def get_cheapest_flight(self):
        cheapest_flight = None
        cheapest_price = float('inf')

        today = datetime.today()
        dates = [(today + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(0, 180, 2)]  # Check every 2nd day

        def fetch_for_date(date):
            retries = 3
            while retries > 0:
                flight_data = self.fetch_flight_data(departure="LON", destination="PAR", departure_date=date)
                if flight_data:
                    return self.get_daily_cheapest_flight(flight_data)
                retries -= 1
                if retries > 0:
                    print(f"Retrying... ({3 - retries}/3)")
                    time.sleep(5)  # Wait for 5 seconds before retrying
            return None

        with ThreadPoolExecutor(max_workers=5) as executor:  # Adjust max_workers as needed
            futures = {executor.submit(fetch_for_date, date): date for date in dates}
            for future in as_completed(futures):
                flight = future.result()
                if flight and flight.price != 'N/A' and float(flight.price) < cheapest_price:
                    cheapest_price = float(flight.price)
                    cheapest_flight = flight

        return cheapest_flight

# Find the cheapest flight over the next 6 months
flight_data_instance = FlightData()
cheapest_flight = flight_data_instance.get_cheapest_flight()

if cheapest_flight:
    print("Cheapest flight found:")
    print(cheapest_flight)
else:
    print("No flights found.")
