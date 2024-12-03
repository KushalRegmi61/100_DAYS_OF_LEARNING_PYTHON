from flask import Flask, render_template, request, flash, redirect, url_for, jsonify, session
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
import requests
from pprint import pprint
import json

# Create a Flask app
app = Flask(__name__)  # Create a Flask app
app.secret_key = "your_secret_key"
Bootstrap5(app)  # Initialize Bootstrap


# New function to fetch the word meaning
def fetch_word_meaning(word):
    try:
        response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return None
    except requests.exceptions.RequestException as e:
        return None

# Flask-WTF Form
class SearchForm(FlaskForm):
    data = StringField(
        "Enter the Word:",
        validators=[
            DataRequired(message="Please enter a word."),
            Length(min=1, max=50, message="Word must be between 1 and 50 characters.")
        ],
        render_kw={
            "placeholder": "Enter the word here (1-50 characters)",
            "style": "width: 100%; margin: 10px 0px 10px 0px;"
        }
    )
    submit = SubmitField("Search" ,render_kw={"class": "btn btn-primary py-2"})

# Home route
@app.route("/", methods=["GET", "POST"])
def home():
    search_form = SearchForm()
    if search_form.validate_on_submit():
        word = search_form.data.data.strip()
        data = fetch_word_meaning(word)
        if data:
            return redirect(url_for("wordmeaning", word=word))
        else:
            flash("Word not found or an error occurred. Please try another.", "danger")
            return redirect(url_for("home"))
        
    return render_template("homepage.html", search_form=search_form)


# Word Meaning Route
@app.route("/wordmeaning", methods=["GET", "POST"])
def wordmeaning():
    word = request.args.get("word")  # Get the word from the URL query parameters
    session['data'] = fetch_word_meaning(word)  # Store the word meaning in the session
    data = session.get("data")  # Fetch the word meaning from the session
    if not data:
        flash("Word not found or an error occurred. Please try another.", "danger")
        return redirect(url_for("home"))
    # Render the page with form and data
    return render_template("wordmeaning.html", data=session['data'])

#TODO: REMAINING TASKS TO BE DONE
# add the favicon
# add the links for footer and header
# add the logo for navbar and improve the navbar
# host the website on render.com

# Run the app
if __name__ == "__main__":
    app.run(debug=True, port=5000)
