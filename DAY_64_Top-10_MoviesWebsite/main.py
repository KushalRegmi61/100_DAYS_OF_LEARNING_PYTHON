from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, NumberRange
import requests
from flask_wtf import FlaskForm


ACCESS_TOKEN='eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyNzQ0MDhhMGI4ODJjNjUwOGM5ZTJlZjg1MTZjMDQ5ZiIsIm5iZiI6MTcyMzU5NTQxOC41MTQ5NTksInN1YiI6IjY2YmJmOTgyMWVlYjA3YzY5ODY2NDM4NyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.3XnrEjyugd2c4h4EGEI7tsE_0J4t2jo0IL26Zxs2gVg'


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

    # rating = FloatField('Rating', validators=[
    #     DataRequired(message="Rating cannot be empty."),
    #     NumberRange(min=0, max=10, message="Rating must be between 0 and 10.")
    # ])

#Edit Movie Rating Form:
class EditRating(FlaskForm):
    rating=FloatField('Your rating out of 10, Eg: 7.5', 
                      validators=[
                                    DataRequired(message="Field cannot be empty."),
                                    NumberRange(min=0, max=10, message="Rating must be between 0 and 10.")                                
                                ])
    review= StringField("Your review.", validators=[DataRequired(message="Field cannot be empty.")])
    submit= SubmitField('Update', render_kw={"size":30})

#Movie Title rating form
class MovieForm(FlaskForm):
    title=StringField("Movie Title", validators=[DataRequired()])
    submit= SubmitField("Add Movie", render_kw={"size":30})

##CREATE DB
class Base(DeclarativeBase):
    pass
#intializing the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


##CREATE TABLE
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

#TODO METHOD TO RENDER HOMEPAGE OF THE WEBSITE
@app.route("/")
def home():
    result = db.session.execute(db.select(Movie))
    all_movies = result.scalars().all()
    return render_template("index.html", movies=all_movies)


#TODO METHOD TO EDIT A MOVIE FROM THE DATABASE
@app.route("/edit_movie", methods=['POST', 'GET'])
def edit():
    movie_id = request.args.get("id")
    form = EditRating()
    item_to_update= db.get_or_404(Movie, movie_id)
    
    if form.validate_on_submit():
        item_to_update.rating=form.rating.data
        item_to_update.review=form.review.data
        # with app.app_context():
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('edit.html', form = form)

#TODO METHOD TO DELETE A MOVIE FROM THE DATABASE
@app.route("/delete/<int:id>")
def delete(id):
     
    item_to_delete=Movie.query.get_or_404(id) #item_to_update= db.get_or_404(Movie, movie_id)
    db.session.delete(item_to_delete)
    db.session.commit()

    return redirect(url_for('home'))

#TODO method to add a movie to the database
@app.route("/add_movie" , methods=['POST', 'GET'])
def add_movie():
    form = MovieForm()

    if form.validate_on_submit():
        movie_title=form.title.data

    return render_template('add.html', form =form)    


if __name__ == '__main__':
    app.run(debug=True)