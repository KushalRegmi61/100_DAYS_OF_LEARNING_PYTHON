from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, ValidationError, Email, Length
from flask_ckeditor import CKEditorField
import re


# Custom validator function
def validate_special_characters(form, field):
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', field.data):
        raise ValidationError("Password must contain at least one special character.")
    

# creating a RegisterForm to register new users
class RegisterForm(FlaskForm):
    name= StringField('Username', 
                      validators=[DataRequired()],
                      render_kw={"size": 30, "placeholder": "Enter your name"}
                      )
    email = StringField('Email', render_kw={"size": 30, "placeholder": "Enter your email"},
                         validators=[DataRequired(), Email()]
                         )
    password = PasswordField('Password',
                         validators=[
                                        DataRequired(),
                                        Length(min=8, message="Too short. Must have 8 characters."),
                                        validate_special_characters
                                    ],
                            render_kw={"size": 30, "placeholder": "Enter your password"}

    )
    address = StringField('Address', validators=[DataRequired()], render_kw={"size": 30, "placeholder": "Enter your address"})

    phone_number = StringField('Phone Number', validators=[DataRequired()], render_kw={"size": 30, "placeholder": "Enter your phone number"})
    submit = SubmitField(label="SignMe up!", render_kw={"size": 30})


# creating a LoginForm to login existing users
class LoginForm(FlaskForm):
    email = StringField('Email', render_kw={"size": 30}, validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField(label="Log In", render_kw={"size": 30})