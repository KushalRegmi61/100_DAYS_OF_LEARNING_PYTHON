from flask import Flask, render_template , request 
import requests
import datetime
import smtplib
import os
from dotenv import load_dotenv
load_dotenv()

EMAIL=os.getenv('my_email')
PASSWORD=os.getenv('EMAIL_PASSWORD')



current_year = datetime.datetime.now().year
today_date = datetime.datetime.now().strftime('%d %B')

app = Flask(__name__)
#loading data
link="https://api.npoint.io/674f5423f73deab1e9a7"
respone=requests.get(link)
data=respone.json()
# print(data)


@app.route('/')
def home():
    return render_template("index.html", blog_data=data , current_year= current_year , today_date=today_date)

@app.route('/aboutme')
def aboutme():
    return render_template('about.html')



@app.route('/post/<blog_id>')
def read_blog(blog_id):
    return render_template("post.html", id=int(blog_id)-1, blog_data=data)

@app.route('/older_post')
def older_post():
    return render_template("olderpost.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        name=data["name"]
        email=data["email"]
        phone_no=data["phone"]
        message=data["message"]
        
        msg_data=(
            f"Subject: New Msg Alert\n\n"
            f"Name: {name}\n"
            f"Email: {email}\n"
            f"Phone_NO: {phone_no}\n"
            f"{message}"
        )
        #sending email....
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=email, to_addrs="kushalbro82@gmail.com", msg=msg_data)

            
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)
if __name__ == "__main__":
    app.run(debug=True)
    
