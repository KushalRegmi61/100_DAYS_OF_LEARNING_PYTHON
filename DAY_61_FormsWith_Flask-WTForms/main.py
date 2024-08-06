from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired, Email, Length, ValidationError
import re
from flask_bootstrap import Bootstrap5

# Custom validator function
def validate_special_characters(form, field):
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', field.data):
        raise ValidationError("Password must contain at least one special character.")

# Creating form class
class LoginForm(FlaskForm):
    email = StringField('Email', render_kw={"size": 30}, validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=8, message="Too short. Must have 8 characters."),
        validate_special_characters
    ])
    submit = SubmitField(label="Log In", render_kw={"size": 30})

app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.secret_key = "Kushal@1"  # Use a more secure method for setting secret keys in production

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@gmail.com" and form.password.data == "Kushal@1":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template("login.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)
