from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, PasswordField
from wtforms.validators import DataRequired, URL, Email, Length, ValidationError
import csv
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


# Custom validator function
def validate_special_characters(form, field):
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', field.data):
        raise ValidationError("Password must contain at least one special character.")

# Creating LOgin_form class
class LoginForm(FlaskForm):
    email = StringField('Email', render_kw={"size": 30}, validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=8, message="Too short. Must have 8 characters."),
        validate_special_characters
    ])
    submit = SubmitField(label="Log In", render_kw={"size": 30})


@app.route("/login", methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@gmail.com" and form.password.data == "Kushal@1":
            return redirect(url_for('add_cafe'))
        else:
            return render_template('denied.html')
    return render_template("login.html", form=form)



# Creating CafeForm class
class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    locationURL = StringField('Cafe Location on Google Map (URL)', validators=[DataRequired(), URL()])
    openTime = StringField('Open Time (e.g. 8AM)', validators=[DataRequired()])
    closeTime = StringField('Closing Time (e.g. 10PM)', validators=[DataRequired()])
    coffeeRating = SelectField('Coffee Rating', choices=[
        ( '☕️'),
        ( '☕️☕️'),
        ( '☕️☕️☕️'),
        ( '☕️☕️☕️☕️'),
        ( '☕️☕️☕️☕️☕️')
    ], validators=[DataRequired()])
    wifiRating = SelectField('Wifi Speed', choices=[
        ('✘'),
        ('💪'),
        ('💪💪'),
        ('💪💪💪'),
        ('💪💪💪💪'),
        ('💪💪💪💪💪')
    ], validators=[DataRequired()])
    powerOutlet = SelectField('Power Socket Availability', choices=[
        ('✘'),
        ( '🔌'),
        ( '🔌🔌'),
        ( '🔌🔌🔌'),
        ( '🔌🔌🔌🔌'),
        ( '🔌🔌🔌🔌🔌')
    ], validators=[DataRequired()])
    submit = SubmitField('Submit')

# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")

#method to add new_cafe
@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        new_row = [
            form.cafe.data,
            form.locationURL.data,
            form.openTime.data,
            form.closeTime.data,
            form.coffeeRating.data,
            form.wifiRating.data, 
            form.powerOutlet.data
        ]
        with open(r"DAY_62_Coffee_\cafe-data.csv", encoding='utf-8', mode='a') as csv_file:
            writer = csv.writer(csv_file)
            # writing new_row 
            writer.writerow(new_row)
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)

@app.route('/cafes')
def cafes():
    with open(r"DAY_62_Coffee_\cafe-data.csv", newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)

if __name__ == '__main__':
    app.run(debug=True)
