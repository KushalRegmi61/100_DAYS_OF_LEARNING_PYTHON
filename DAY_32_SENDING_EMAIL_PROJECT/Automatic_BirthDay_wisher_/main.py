import smtplib
import random
import datetime as dt
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

my_email = os.getenv("my_email")  # My email ID
my_password = os.getenv("EMAIL_PASSWORD")  # Email password

# Create a datetime object
time = dt.datetime.now()
today_tuple = (time.day, time.month)

# TODO 1: Open the birthday CSV file and read birthdays from it
df = pd.read_csv("DAY_32_SENDING_EMAIL_PROJECT/Automatic_BirthDay_wisher_/birthdays.csv")

# Create a dictionary of birthdays
birthdays_dict = {(row.day, row.month): row for (index, row) in df.iterrows()}

# TODO 2: Check if today's date matches any birthdays
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    with open(f"DAY_32_SENDING_EMAIL_PROJECT/Automatic_BirthDay_wisher_/letter_templates/letter_{random.randint(1, 3)}.txt") as letter_file:
        text_msg = letter_file.read()
        text_msg = text_msg.replace("[NAME]", birthday_person['name'])

    # TODO 3: Send the email
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person['email'],
            msg=f"Subject: Happy Birthday!.... :) \n\n{text_msg}"
        )
