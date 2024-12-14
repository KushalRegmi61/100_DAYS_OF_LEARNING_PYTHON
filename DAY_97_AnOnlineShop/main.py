from datetime import date
from hashlib import md5
from flask import Flask, abort, render_template, redirect, url_for, flash, request,current_app, session
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
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
# importing forms from forms.py
from forms import RegisterForm, LoginForm


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
# initializing the flask ckeck editor
CKEditor(app)

# # Configure Flask Login
login_manager = LoginManager()
login_manager.init_app(app)

# # Load user
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


# creating a declearative base
class Base(DeclarativeBase):
    pass

# connect to the database

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", "sqlite:///shop.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# creating the database
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# creating a user class
class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(100), nullable=False)
    # orders = db.relationship('Order', back_populates='user')


# Initializing the database
with app.app_context():
    db.create_all()


# creating homepage route
@app.route('/')
def home():
    return render_template('homepage.html')


# creating a route for user registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        address = form.address.data
        phone_number = form.phone_number.data
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
        new_user = User(name=name, email=email, password=hashed_password, address=address, phone_number=phone_number)
        db.session.add(new_user)
        db.session.commit()
        flash("You have successfully registered.login to continue.", 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


# creating a route for user login
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user)
                flash(f"{current_user.name} Logged in successfully.", 'success')
                return redirect(url_for('home'))
            else:
                flash("Password incorrect, please try again.", 'danger')
        else:
            flash("Email does not exist, please try again.", "danger")

    return render_template('login.html', form=form)


# creating a route for user logout
@app.route('/logout')
def logout():
    logout_user()
    flash("You have been logged out.", 'success')
    return redirect(url_for('home'))

# runnning the app
if __name__ == "__main__":
    app.run(debug=True, port=5000)



