from flask import Flask, render_template
import requests

app = Flask(__name__)
#loading data
link="https://api.npoint.io/c790b4d5cab58020d391"
respone=requests.get(link)
data=respone.json()


@app.route('/')
def home():

    return render_template("index.html", blog_data=data)

@app.route('/post/<blog_id>')
def read_blog(blog_id):
    return render_template("post.html", id= int(blog_id)-1, blog_data=data)
        


if __name__ == "__main__":
    app.run(debug=True)
