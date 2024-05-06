from dotenv import load_dotenv
import os
import requests
import smtplib

# Load environment variables from .env file
load_dotenv()

my_email = os.getenv("my_email")
openweather_api_key = os.getenv("OPENWEATHER_API_KEY")

receiver_email = ['kushalbro82@gmail.com', 'aditgyawali33@gmail.com', 'nill.aryal49@gmail.com','saunksu@gmail.com']
email_password = os.getenv("EMAIL_PASSWORD")

parameters = {
    "lat": 27.717245,
    "lon": 85.323959,
    "appid": openweather_api_key,
    "cnt": 4
}

response = requests.get(url="http://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_id = [weather_data["list"][i]["weather"][0]["id"] for i in range(len(weather_data["list"]))]
will_rain = any(i < 700 for i in weather_id)

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=email_password)

    if will_rain:
        for i in receiver_email:
            connection.sendmail(
                from_addr=my_email,
                to_addrs=i,
                msg="Subject: RAIN TODAY.... \n\n It will rain today.\nCarry an Umbrella with You..."
            )
    else:
        for i in receiver_email:
            connection.sendmail(
                from_addr=my_email,
                to_addrs=i,
                msg="Subject: NO RAIN TODAY.... \n\n It won't rain today..."
            )
