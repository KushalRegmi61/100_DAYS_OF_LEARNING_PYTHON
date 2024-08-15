from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, NumberRange
import requests
from dotenv import load_dotenv
import os

load_dotenv()

MOVIE_DB_API_KEY = os.getenv('MOVIE_IDB_API_KEY')
MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie?include_adult=false&language=en-US&page=1"

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# Edit Movie Rating Form
class EditRating(FlaskForm):
    rating = FloatField('Your rating out of 10, Eg: 7.5', 
                        validators=[
                            DataRequired(message="Field cannot be empty."),
                            NumberRange(min=0, max=10, message="Rating must be between 0 and 10.")
                        ])
    review = StringField("Your review.", validators=[DataRequired(message="Field cannot be empty.")])
    submit = SubmitField('Update', render_kw={"size":30})

# Movie Title Rating Form
class MovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie", render_kw={"size":30})

# Create DB
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Create Table
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

with app.app_context():
    db.create_all()

# Homepage Route
@app.route("/")
def home():
    result = db.session.execute(db.select(Movie))
    all_movies = result.scalars().all()
    return render_template("index.html", movies=all_movies)

# Edit Movie Route
@app.route("/edit_movie", methods=['POST', 'GET'])
def edit():
    movie_id = request.args.get("id")
    form = EditRating()
    item_to_update = db.get_or_404(Movie, movie_id)
    
    if form.validate_on_submit():
        item_to_update.rating = form.rating.data
        item_to_update.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('edit.html', form=form)

# Delete Movie Route
@app.route("/delete/<int:id>")
def delete(id):
    item_to_delete = Movie.query.get_or_404(id)
    db.session.delete(item_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

# Add Movie Route
@app.route("/add_movie", methods=['POST', 'GET'])
def add_movie():
    form = MovieForm()

    if form.validate_on_submit():
        movie_title = form.title.data
        response = requests.get(MOVIE_DB_SEARCH_URL, params={"api_key": MOVIE_DB_API_KEY, "query": movie_title})
        data = response.json().get("results", [])

        return render_template("select.html", options=data)
    
    return render_template('add.html', form=form)

# Search Movie Route
@app.route("/search")
def search():
    movie_id = request.args.get('movie_id')
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {os.getenv('ACCESS_TOKEN')}"  
    }

    response = requests.get(url, headers=headers)
    movie_data = response.json()
    
    title = movie_data.get('title')
    poster_path = movie_data.get('poster_path')
    release_date = movie_data.get('release_date')
    description = movie_data.get('overview')
    img_url = f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else None
    year = release_date.split('-')[0] if release_date else 'Unknown Year'

    # Adding new movie to the database
    if not Movie.query.filter_by(title=title).first():  # Check if the movie already exists
        new_movie = Movie(title=title, year=year, description=description, img_url=img_url)
        db.session.add(new_movie)
        db.session.commit()
        #assign the movie id after comming it to the database
        movie_no=new_movie.id

    return redirect(url_for('edit', id=movie_no))

if __name__ == '__main__':
    app.run(debug=True)



# # After adding the new_movie the code needs to be commented out/deleted.
# # So you are not trying to add the same movie twice.
# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# second_movie = Movie(
#     title="Avatar The Way of Water",
#     year=2022,
#     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#     rating=7.3,
#     ranking=9,
#     review="I liked the water.",
#     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
# )
# with app.app_context():
#     db.session.add(new_movie)
#     db.session.add(second_movie)
#     db.session.commit()
