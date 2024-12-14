from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, FileField, DecimalField
from wtforms.validators import DataRequired, URL, ValidationError, Email, Length, NumberRange
from flask_wtf.file import FileField, FileAllowed
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


class AddProductForm(FlaskForm):
    name = StringField('Product Name',
                       validators=[DataRequired()],
                       render_kw={"size": 30, "placeholder": "Enter product name"}
                       )
    category = StringField('Category',
                           validators=[DataRequired()],
                           render_kw={"size": 30, "placeholder": "Enter product category Eg. Basin, Towel"}
                           )
    price = DecimalField('Price',
                         validators=[DataRequired(), NumberRange(min=0, message="Price must be a positive number")],
                         render_kw={"size": 30, "placeholder": "Enter product price in Nrs. Eg. 1000"}
                         )
    description = CKEditorField('Description',
                                validators=[DataRequired()],
                                render_kw={"size": 30, "placeholder": "Enter product description"}
                                )
    image_url = FileField('Image',
                          validators=[DataRequired(), FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!')],
                          render_kw={"size": 30, "placeholder": "Choose an image file"}
                          )
    submit = SubmitField(label="Add Product", render_kw={"size": 30})

# creating a form to update product
class UpdateProductForm(FlaskForm):
    name =  StringField('Product Name', 
                        validators=[DataRequired()],
                         render_kw={"size": 30, "placeholder": "Enter product name"}
                         )
    category = StringField('Category',
                            validators=[DataRequired()],
                            render_kw={"size": 30, "placeholder": "Enter product category Eg. Basin, Towel"}
                            )
    
    price = StringField('Price',
                        validators=[DataRequired()],
                        render_kw={"size": 30, "placeholder": "Enter product price in Nrs. Eg. 1000"}
                        )
    
    description = CKEditorField('Description', 
                                validators=[DataRequired()],
                                render_kw={"size": 30, "placeholder": "Enter product description"}
                                )
    
    image_url = FileField('Image URL',
                            validators=[DataRequired(), URL()],
                            render_kw={"size": 30, "placeholder": "Choose an image file"}
                            )
    
    submit = SubmitField(label="Update Product", render_kw={"size": 30})
                          

