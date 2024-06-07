from flight_search import FlightSearch
class FlightData:
    def __init__(self, price=None, departure_airport_code=None, destination_airport_code=None, departure_date=None, return_date=None, airline_name=None):
        self.price = price
        self.departure_airport_code = departure_airport_code
        self.destination_airport_code = destination_airport_code
        self.departure_date = departure_date
        self.return_date = return_date
        self.airline_name = airline_name

    def __repr__(self):
        return (f"FlightData(price={self.price}, departure_airport_code={self.departure_airport_code}, "
                f"destination_airport_code={self.destination_airport_code}, departure_date={self.departure_date}, "
                f"return_date={self.return_date}, departure_airport_name={self.departure_airport_name}, "
                f"destination_airport_name={self.destination_airport_name}, airline_name={self.airline_name})")

    @staticmethod
    def find_cheapest_flight(flight_data):
        if flight_data is None:
            return None  # Return None if no flight data available

        offers = flight_data.get("data", [])
        if not offers:
            return FlightData(price='N/A',
                              departure_airport_code='N/A',
                              destination_airport_code='N/A',
                              departure_date='N/A',
                              return_date='N/A',
                              airline_name='N/A'
                              )

        cheapest_offer = min(offers, key=lambda x: x.get("price", {}).get("total"))

        # Extract flight details from the cheapest offer
        segments = cheapest_offer.get("itineraries", [])[0].get("segments", [])
        if not segments:
            return FlightData(price='N/A',
                              departure_airport_code='N/A',
                              destination_airport_code='N/A',
                              departure_date='N/A',
                              return_date='N/A',
                              departure_airport_name='N/A',
                              destination_airport_name='N/A',
                              airline_name='N/A'
                              )

        departure_segment = segments[0]
        arrival_segment = segments[-1]

        departure_airport_code = departure_segment.get("departure", {}).get("iataCode")
        destination_airport_code = arrival_segment.get("arrival", {}).get("iataCode")
        departure_date = departure_segment.get("departure", {}).get("at")
        return_date = arrival_segment.get("arrival", {}).get("at")
        price = cheapest_offer.get("price", {}).get("total")

        
        # Extract airline name
        airline_code = departure_segment.get("carrierCode")
        airline_name = flight_data.get("dictionaries", {}).get("carriers", {}).get(airline_code)

        # Create and return a FlightData object
        return FlightData(price=price,
                          departure_airport_code=departure_airport_code,
                          destination_airport_code=destination_airport_code,
                          departure_date=departure_date,
                          return_date=return_date,
                          airline_name=airline_name
                          )

