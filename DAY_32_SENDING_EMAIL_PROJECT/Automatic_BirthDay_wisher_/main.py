##################### Birthday  E-mail Project ######################
import smtplib
import random
import datetime as dt
import pandas

my_email = "nepmrkush@gmail.com" #my email id
my_password= "audj quhv eyky ejlq" #random id password

#creating a datetime class object
time = dt.datetime.now()
today_tuple = (time.day,time.month)

#TODO 1 OPENING BIRTHDAY CSV FILE TO READ BIRTHDAY FORM IT
df = pandas.read_csv(r"DAY_32_SENDING_EMAIL_PROJECT\Automatic_BirthDay_wisher_\birthdays.csv")

#creating birthdays_dict
birthdays_dict = {(row.day, row.month):row for (index, row) in df.iterrows()}

    
#TODO_2 checking if the date/month matches
if today_tuple in birthdays_dict: 
    brithday_person = birthdays_dict[today_tuple]
    with open(f"DAY_32_SENDING_EMAIL_PROJECT\Automatic_BirthDay_wisher_\letter_templates\letter_{random.randint(1,3)}.txt")  as letter_file:
        text_msg = letter_file.read() 
        text_msg =text_msg.replace("[NAME]", brithday_person['name'])

#TODO _ 3 SENDING EMAIL TO PERSON        
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user  = my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=brithday_person['email'],                    
        msg=f"Subject: Happy Birthday!.... :) \n\n{text_msg}")
  




