from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import datetime

# Initializing Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
ckeditor = CKEditor(app)

# Create database
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app, model_class=Base)

# Configure table
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

with app.app_context():
    db.create_all()

# WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Author's Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField('Blog Content', validators=[DataRequired()])
    submit = SubmitField("Submit Post")

@app.route('/')
def get_all_posts():
    # Query the database for all the posts and convert to a python list
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts)

@app.route("/post/<int:post_id>")
def show_post(post_id):
    # Retrieve a BlogPost from the database based on the post_id
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)

# Adding a new Post
@app.route("/new-post", methods=["GET", "POST"])
def add_new_post():
    form = CreatePostForm()
    
    if form.validate_on_submit():
        newPost = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            date=datetime.now().strftime('%B %d, %Y'),
            body=form.body.data,
            author=form.author.data,
            img_url=form.img_url.data
        )
        db.session.add(newPost)
        db.session.commit()

        return redirect(url_for('get_all_posts'))

    return render_template("make-post.html", form=form, title="New Post")

# TODO: Method to edit the post
@app.route('/edit-post/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    item_to_edit = db.session.get(BlogPost, post_id)  # Retrieve the post using the post_id
    if not item_to_edit:
        # Handle the case if the post is not found
        return "Post not found", 404

    form = CreatePostForm(obj=item_to_edit)  # Pre-populate form with existing data

    if form.validate_on_submit():
        # Update the post with form data
        item_to_edit.title = form.title.data
        item_to_edit.subtitle = form.subtitle.data
        # item_to_edit.date = datetime.now().strftime('%B %d, %Y') Date should not be updated
        item_to_edit.body = form.body.data
        item_to_edit.author = form.author.data
        item_to_edit.img_url = form.img_url.data

        db.session.commit()  # Commit changes to the database
        return redirect(url_for('get_all_posts'))  # Redirect to the list of posts

    return render_template('make-post.html', form=form, title="Edit Post")

#TODO METHOD TO DELETE POST
@app.route("/delete_post/<int:post_id>")
def delete_post(post_id):
    post_to_delete=db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()

    return redirect(url_for('get_all_posts'))


#TODO METHOD TO SHOW ABOUT THE WEBSITE
@app.route("/about")
def about():
    return render_template("about.html")

#TODO METHOD TO SHOW CONTACT DETAILS
@app.route("/contact")
def contact():
    return render_template("contact.html")

#TODO METHOD TO DISPLAY OLDER POSTS
@app.route('/older_post')
def older_post():
    return render_template("olderpost.html")

if __name__ == "__main__":
    app.run(debug=True, port=5001)
