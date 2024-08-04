from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired, Email, Length, ValidationError
import re

# Custom validator function
def validate_special_characters(form, field):
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', field.data):
        raise ValidationError("Password must contain at least one special character.")


#creating form class
class LoginForm(FlaskForm):
    email = StringField('Email',render_kw={"size":30}, validators=[DataRequired(),Email() ])
    password = PasswordField('Password', validators=[
                        DataRequired(),
                        Length(min=8, message="Too Short. Must Have 8 characters."),
                        validate_special_characters
                        ]
                        )
    submit= SubmitField(label="Log IN", render_kw={"size":30})


app = Flask(__name__)
app.secret_key="Kushal@1"

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['POST', 'GET'])
def login():
    form = LoginForm()
    form.validate_on_submit()
    return render_template("login.html", form = form)


if __name__ == '__main__':
    app.run(debug=True)
