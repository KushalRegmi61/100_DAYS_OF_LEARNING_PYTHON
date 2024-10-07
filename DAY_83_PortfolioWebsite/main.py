from flask import Flask, render_template, request, redirect
from datetime import datetime
from flask_bootstrap import Bootstrap5

#creating a flask app
app = Flask(__name__)

#creating home page 
@app.route('/')
def home():
    return render_template("index.html")

#creating page page
@app.route('/projects')
def projects():
    return render_template("projects.html")

#creating contact page and passing contact form data to the server
@app.route('/contact')
def contact():
    return render_template("contact.html")

#degug the website 
if __name__ == "__main__":
    app.run(debug=True , port=5000)

#<header
#   class="masthead"
#   style="background-image: url('../static/assets/img/home-bg.jpg')"
# >