from flask import Flask, render_template
import requests
import datetime


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
@app.route('/contactme')
def contactme():
    return render_template('contact.html')



@app.route('/post/<blog_id>')
def read_blog(blog_id):
    return render_template("post.html", id=int(blog_id)-1, blog_data=data)

@app.route('/older_post')
def older_post():
    return render_template("olderpost.html")

        


if __name__ == "__main__":
    app.run(debug=True)
    
