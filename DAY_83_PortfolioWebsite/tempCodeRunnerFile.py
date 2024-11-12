from flask import Flask, render_template, request, redirect
from datetime import datetime
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, ValidationError, Email, Length