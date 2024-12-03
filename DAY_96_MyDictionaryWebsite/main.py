from flask import Flask, render_template, request, flash, redirect, url_for, session
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

import requests


# Create a Flask app
app = Flask(__name__) # Create a Flask app
app.secret_key = "your_secret_key"
Bootstrap5(app)  # Initialize Bootstrap


# Flask-WTF Form
class SearchForm(FlaskForm):
    data = StringField("Enter the Word:", validators=[DataRequired(message="Please enter a word."), Length(min=1, max=50, message="Word must be between 1 and 50 characters.")])
    submit = SubmitField("Search")






data = input('Enter the data: ')


response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{data}")

response.raise_for_status()
print(response.status_code)
print(response.json())
