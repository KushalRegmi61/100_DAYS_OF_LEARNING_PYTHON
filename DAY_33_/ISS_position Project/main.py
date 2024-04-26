import requests
from datetime import datetime
import smtplib
import time

my_email = "nepmrkush@gmail.com"  # Your email id
my_password = "audj quhv eyky ejlq"  # Random id password

MY_LAT = 27.666620  # Your latitude
MY_LONG = 85.333328  # Your longitude

# Function to check if the ISS is close to user's current position
def check_position():
    try:
        response = requests.get(url="http://api.open-notify.org/iss-now.json")
        response.raise_for_status()
        data = response.json()
        iss_latitude = float(data["iss_position"]["latitude"])
        iss_longitude = float(data["iss_position"]["longitude"])
        print(iss_latitude, iss_longitude)
        if abs(MY_LAT - iss_latitude) <= 5 and abs(MY_LONG - iss_longitude) <= 5:
            return True
        else:
            return False
    except Exception as e:
        print("Error occurred while fetching ISS position:", e)
        return False

#function to check time 
def check_time():
    parameters = {
    "lat" :MY_LAT, 
    "lng" : MY_LONG, 
    "formatted": 0   
    }
    response_2 = requests.get(url= f"https://api.sunrise-sunset.org/json", params= parameters)
    response_2.raise_for_status()
    data_2 = response_2.json()
    sunrise = int(data_2["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data_2["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = int(datetime.now().hour)
    if time_now>= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(6)
    if check_time() and check_position():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs=my_email,
                                msg="Subject: Look Up In The Sky!\n\nISS Satellite is near your location!")
        
        