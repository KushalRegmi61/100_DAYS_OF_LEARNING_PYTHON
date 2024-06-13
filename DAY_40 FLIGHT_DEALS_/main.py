import os
from dotenv import load_dotenv
from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
from datetime import datetime

load_dotenv()

#GLOBAL VARIABLE SECTION 
DATE= datetime.today().strftime('%Y-%m-%d')
DEPARATURE_LOCATION=input("Enter The Departure Loacation:").title()
DEPRATURE_LOCATION_IATA_CODE= None


datamanager= DataManager()#datamanger class object
flightsearch= FlightSearch()#flight manager class object
flightdata = FlightData()#flight data class object
notifiactionmanager = NotificationManager()


#TODO  UPDATING THE USER_DETAILS IN THE SHEET
while True:
    print("\nWelcome to the Kushal's Flight Club.\nWe find best flight deals and email you.")
    fname= input("Enter  your First Name: ").title()
    lname= input("Enter your First Name: ").title()
    email_1=input("Enter  your Email: ")
    email_2=input("Re-Enter the Email: ")
    if email_1==email_2:
        datamanager.insert_userDetails(firstName=fname, lastName=lname,email=email_2)
    else:
        print("\nPlease, Re-Check your Email and try again.")    
        
    choice=input("Do you add another user details?(Yes/No): ").lower()
    if choice=="yes" or choice=="y":
        break

#GETTING THE USER DATA FROM USERDETAILS SPREADSHEET
user_data = datamanager.get_user_data()


#getting hold of departure location IATA code
DEPRATURE_LOCATION_IATA_CODE =flightsearch.iata_code(DEPARATURE_LOCATION)


# #TODO CHECKING IF DEPRATURE_LOCATION_IATA_CODE IS AVALIABLE IN THE API OR NOT 
if DEPRATURE_LOCATION_IATA_CODE == None:
    print("\nSorry! IATA code is NOT avaliable in the API :( \nHINTS: Enter the IATA CODE manually from google..")
    DEPRATURE_LOCATION_IATA_CODE= input(f"\nEnter the IATA code of {DEPARATURE_LOCATION} city: ").upper()

#getting the data stored in the Price spreadsheet ....
sheet_data = datamanager.get_data()

a =-1
# using flight_data to insert iataCode to the sheet
for data in sheet_data:
    if data['iataCode']=="":
        a = sheet_data.index(data)
        data['iataCode']=flightsearch.iata_code(cityname=data['city'])
                   
#updating the iataCode to the Google Sheet 
if a>=0:
    datamanager.destination_data = sheet_data
    datamanager.update_destination_codes()
    
#checking the flights avaliable     
for data in sheet_data:

    cheapest_flight=flightdata.get_cheapest_flight(dep_location="LON",
                                                   des_location="NYC"
                                                   ) 
    
    
    try:
       #checking wheather there is transit location or not
        if cheapest_flight.transit_city_name==None : 
            message_body = (
                        f"Only £{cheapest_flight.price} to fly with {cheapest_flight.airline_name} from {DEPARATURE_LOCATION.upper()} ({cheapest_flight.departure_airport_code})"
                        f" to {data['city'].upper()} ({cheapest_flight.destination_airport_code}), "
                        f"on {cheapest_flight.departure_date.split('T')[0]} until {cheapest_flight.return_date.split('T')[0]}."
                        )
        else:
            message_body = (
                        f"Only £{cheapest_flight.price} to fly with {cheapest_flight.airline_name} from {DEPARATURE_LOCATION.upper()} ({cheapest_flight.departure_airport_code})"
                        f" to {data['city'].upper()} ({cheapest_flight.destination_airport_code}), "
                        f"on {cheapest_flight.departure_date.split('T')[0]},Bookings until {cheapest_flight.last_ticketing_date.split('T')[0]}."
                        f"Flight has one stop, via {cheapest_flight.transit_city_name}"
                        )
            
        if cheapest_flight.price != "N/A" and float(cheapest_flight.price)<= float(data['lowestPrice']):
            for details in user_data:
                notifiactionmanager.send_email(fname=details['firstName'],
                                               lname=details['lastName'],
                                               email=details['email'],
                                               message=message_body
                                               )
        
    except AttributeError as e:
        pass 
        

