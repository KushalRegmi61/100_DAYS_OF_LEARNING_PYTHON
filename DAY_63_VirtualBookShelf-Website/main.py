from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange

app = Flask(__name__)
bootstrap = Bootstrap(app)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
db = SQLAlchemy(app)

# Define the Book model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'

# Create the table schema in the database
with app.app_context():
    db.create_all()

app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

# Create the form class
class RatingForm(FlaskForm):
    rating = FloatField('Rating', validators=[
        DataRequired(message="Rating cannot be empty."),
        NumberRange(min=0, max=10, message="Rating must be between 0 and 10.")
    ])
    submit = SubmitField(label="Change Rating")

@app.route('/')
def home():
    with app.app_context():
        all_books = Book.query.order_by(Book.title).all()
    return render_template('index.html', books=all_books)

@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        data = request.form
        book_name = data['BookName']
        author = data['Author']
        rating = float(data['Rating'])

        # Create a new book record
        new_book = Book(title=book_name, author=author, rating=rating)
        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for('home'))

    return render_template('add.html')

@app.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit(id):
    form = RatingForm()
    book_to_update = Book.query.get_or_404(id)

    if request.method == 'POST':
        book_to_update.rating = form.rating.data
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('edit.html', form=form, book=book_to_update)

@app.route('/delete/<int:id>')
def delete(id):
    book_to_delete = Book.query.get_or_404(id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
