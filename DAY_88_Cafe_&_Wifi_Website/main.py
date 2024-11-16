from flask import Flask, render_template, request, redirect, session
from datetime import datetime
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, ValidationError, Email, Length
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, ForeignKey, Column, func
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, RadioField
from wtforms.validators import DataRequired, URL, ValidationError, Email, Length
from flask_ckeditor import CKEditorField

#creating a flask app
app = Flask(__name__)

# initilizing the bootstrap
Bootstrap5(app)

#creating a secret key
app.config['SECRET_KEY'] = "8BYkEfBA"

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
    __tablename__ = "cafe"
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
    country = db.Column(db.String(250), nullable=False)
    city = db.Column(db.String(250), nullable=False)

#creating a form for adding a new cafe
class AddCafeForm(FlaskForm):
    name = StringField("Cafe Name", validators=[DataRequired()])
    country = StringField("Country", validators=[DataRequired()])
    city = StringField("City", validators=[DataRequired()])
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
    return render_template('index.html')

#Explore cafe_route
@app.route('/explore_cafe')
def explore_cafe():    
    # Get distinct countries from the cafes table
    countries = db.session.query(Cafes.country).distinct()
    print(countries)
    # Initialize an empty dictionary to store country -> cities mapping
    country_city_dict = {}
    
    # Loop through each country
    for country_tuple in countries:
        country = country_tuple[0]  # Extract the country name from the tuple
        
        # Get all cities associated with this country
        cities = db.session.query(Cafes.city).filter(Cafes.country == country).distinct().all()
        
        # Create a list of cities for the current country
        city_list = [city[0] for city in cities]  # Extract city names from tuples
        
        # Add the country and its cities to the dictionary
        country_city_dict[country] = city_list
    
    # Print or return the dictionary
    print(country_city_dict)

   
    return render_template('explore_cafe.html', countries=country_city_dict)
    

#Add cafe route
@app.route('/add_cafe', methods=['GET', 'POST'])
def add_cafe():
    form = AddCafeForm()
    if form.validate_on_submit():
        try:
            # Attempt to add the new cafe to the database
            new_cafe = Cafes(
                name=form.name.data,
                map_url=form.map_url.data,
                img_url=form.img_url.data,
                location=form.location.data,
                has_sockets=form.has_sockets.data,
                has_toilet=form.has_toilet.data,
                has_wifi=form.has_wifi.data,
                can_take_calls=form.can_take_calls.data,
                seats=form.seats.data,
                coffee_price=form.coffee_price.data,
                country=form.country.data,
                city=form.city.data
            )
            db.session.add(new_cafe)
            db.session.commit()
            
            # Set success message
            session['message'] = "Cafe added successfully!"
            session['message_type'] = 'success'

        except Exception as e:
            # Handle error, set error message
            session['message'] = "There was an issue adding the cafe. Please try again."
            session['message_type'] = 'error'

        # Pop the session message after setting it, and pass the message to the template
        message = session.pop('message', None)
        message_type = session.pop('message_type', None)

        return render_template('add_cafe.html', form=form, message=message, message_type=message_type)

    # If form not submitted, just render the form with no message
    return render_template('add_cafe.html', form=form)


#Delete cafe route
@app.route('/delete_cafe/<int:id>', methods=['GET', 'POST'])
def delete_cafe():
    pass

#search_cafe route
@app.route('/search_cafe/<string:city_name>')
def search_cafe(city_name):
    # Convert city_name from the URL to lowercase
    location_lower = city_name.lower()
    
    # Getting all the cafes from the database with the city_name (case-insensitive)
    cafes = db.session.execute(db.select(Cafes).where(func.lower(Cafes.city) == location_lower)).scalars().all()
    print(cafes)
    return render_template('cafe_list.html', cafes=cafes)


#display_cafe details
@app.route('/cafe/<int:cafe_id>')
def cafe_details(cafe_id):
    cafe = Cafes.query.get_or_404(cafe_id) # Get the cafe with the given ID
    return render_template('cafe_details.html', cafe=cafe)


#running the app
if __name__ == "__main__":
    app.run(debug=True, port=5000)