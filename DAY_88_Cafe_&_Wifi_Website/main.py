from flask import Flask, render_template, request, redirect
from datetime import datetime
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, ValidationError, Email, Length
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, ForeignKey
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, RadioField
from wtforms.validators import DataRequired, URL, ValidationError, Email, Length
from flask_ckeditor import CKEditorField

#creating a flask app
app = Flask(__name__)

# initilizing the bootstrap
Bootstrap5(app)






#creating a declarative database
class Base(DeclarativeBase):
    pass
    

#creating a database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///cafes.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(model_class=Base)
db.init_app(app)

#creating a table for cafes
class Cafes(db.Model):
    __tablename__ = "cafes"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    coffee_price = db.Column(db.String(250), nullable=False)

#creating a form for adding a new cafe
class AddCafeForm(FlaskForm):
    id = StringField("ID", validators=[DataRequired()])
    name = StringField("Cafe Name", validators=[DataRequired()])
    map_url = StringField("Map URL", validators=[DataRequired(), URL()])
    img_url = StringField("Image URL", validators=[DataRequired(), URL()])
    location = StringField("Location", validators=[DataRequired()])
    has_sockets = BooleanField("Has Sockets", validators=[DataRequired()])
    has_toilet = BooleanField("Has Toilet", validators=[DataRequired()])
    has_wifi = BooleanField("Has Wifi", validators=[DataRequired()])
    can_take_calls = BooleanField("Can Take Calls", validators=[DataRequired()])
    seats = StringField("Number of Seats Eg.20-40 seats ", validators=[DataRequired()])
    coffee_price = StringField("Coffee Price", validators=[DataRequired()])
    submit = SubmitField("Add Cafe", render_kw={"size": 30})

#creating a form for editing a cafe
class EditCafeForm(FlaskForm):
    id = StringField("ID", validators=[DataRequired()])
    name = StringField("Cafe Name", validators=[DataRequired()])
    map_url = StringField("Map URL", validators=[DataRequired(), URL()])
    img_url = StringField("Image URL", validators=[DataRequired(), URL()])
    location = StringField("Location", validators=[DataRequired()])
    has_sockets = BooleanField("Has Sockets", validators=[DataRequired()])
    has_toilet = BooleanField("Has Toilet", validators=[DataRequired()])
    has_wifi = BooleanField("Has Wifi", validators=[DataRequired()])
    can_take_calls = BooleanField("Can Take Calls", validators=[DataRequired()])
    seats = StringField("Number of Seats Eg.20-40 seats ", validators=[DataRequired()])
    coffee_price = StringField("Coffee Price", validators=[DataRequired()])
    submit = SubmitField("Update", render_kw={"size": 30})




#initializing the database
with app.app_context():
    db.create_all() 


#home route
@app.route('/')
def home():
    cafes = Cafes.query.all()
    return render_template('index.html', cafes=cafes)



#running the app
if __name__ == "__main__":
    app.run(debug=True, port=5000)