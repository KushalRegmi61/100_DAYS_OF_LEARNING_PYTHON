import smtplib
import random
import datetime as dt
my_email = "nepmrkush@gmail.com"
my_password= "audj quhv eyky ejlq"

time = dt.datetime.now()
day = time.strftime("%A")
print(day)
with open("DAY_32_SENDING_EMAIL_PROJECT\quotes.txt", "r") as datafile:
    # Read the lines, strip whitespace, and store in a list
    quotes = [line.strip() for line in datafile.readlines()]

#generating random quote from the file.... 
quote_of_day = random.choice(quotes)

#sending an email on every wednesday of the week
if day == "Wednesday":
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user  = my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs="kushalbro82@gmail.com",msg=quote_of_day)
        
