from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)

## CREATE DATABASE
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"

# Create the extension
db = SQLAlchemy(model_class=Base)
# Initialize the app with the extension
db.init_app(app)

## CREATE TABLE
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'

# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()

app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

@app.route('/')
def home():
    all_books = []
    with app.app_context():
        result = db.session.execute(db.select(Book).order_by(Book.title))
        all_books = result.scalars().all()
        # print(all_books)
        # for book in books:
        #     all_books.append({'title': book.title, 'author': book.author, 'rating': book.rating})
    return render_template('index.html', books=all_books)

@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        data = request.form
        book_name = data['BookName']
        author = data['Author']
        rating = float(data['Rating'])  # Ensure rating is a float

        # CREATE RECORD
        with app.app_context():
            new_book = Book(title=book_name, author=author, rating=rating)
            db.session.add(new_book)
            db.session.commit()
            
        return redirect(url_for('home'))
    
    return render_template('add.html')

if __name__ == "__main__":
    app.run(debug=True)
