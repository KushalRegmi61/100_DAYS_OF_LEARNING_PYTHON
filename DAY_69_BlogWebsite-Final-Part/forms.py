from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, ValidationError, Email, Length
from flask_ckeditor import CKEditorField
import re


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


# Custom validator function
def validate_special_characters(form, field):
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', field.data):
        raise ValidationError("Password must contain at least one special character.")
    
# TODO: Create a RegisterForm to register new users
class RegisterForm(FlaskForm):
    name= StringField('Username', validators=[DataRequired()])
    email = StringField('Email', render_kw={"size": 30}, validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=8, message="Too short. Must have 8 characters."),
        validate_special_characters
    ])
    submit = SubmitField(label="SignMe up!", render_kw={"size": 30})




# TODO: Create a LoginForm to login existing users
class LoginForm(FlaskForm):
    email = StringField('Email', render_kw={"size": 30}, validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField(label="Log In", render_kw={"size": 30})


# TODO: Create a CommentForm so users can leave comments below posts
class CommentForm(FlaskForm):
    body = CKEditorField('Comment', validators=[DataRequired()])
    submit = SubmitField(label='Post Comment', render_kw={'size':30})

