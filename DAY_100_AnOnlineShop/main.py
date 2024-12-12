from datetime import date
from hashlib import md5
from flask import Flask, abort, render_template, redirect, url_for, flash, request,current_app, session
from flask_bootstrap import Bootstrap5
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy, pagination
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, ForeignKey
from functools import wraps
from typing import List
import hashlib
import smtplib
import os
from dotenv import load_dotenv
from smtplib import SMTP

# Load environment variables
load_dotenv()

# Email and password for the email
MY_EMAIL = os.getenv("EMAIL")
MY_PASSWORD = os.getenv("EMAIL_PASSWORD")


# create a new flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "this-is-a-secret-key")


# create a new bootstrap object
Bootstrap5(app)

# # Configure Flask Login 
# login_manager = LoginManager()
# login_manager.init_app(app)


# # load user 
# @login_manager.user_loader()
# def load_user(user_id):
#     return User.query.get(user_id)

# creating a declearative base
class Base(DeclarativeBase):
    pass

# connect to the database

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", "sqlite:///shop.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# creating the database
db = SQLAlchemy(app)


# creating a default_route
# app.route("/")
# def home():
#     return render_template("homepage.html")


@app.route('/')
def home():
    return render_template('homepage.html')

# runnning the app
if __name__ == "__main__":
    app.run(debug=True, port=5000)



