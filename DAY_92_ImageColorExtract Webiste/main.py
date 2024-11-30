from flask import Flask, render_template, request, flash, redirect, url_for, session
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import DataRequired
import os
from PIL import Image
import numpy as np



# Define helper to extract top colors
def get_top_colors(image_path, top_n=10):
    image = Image.open(image_path).convert('RGB')
    img_arr = np.array(image)
    pixels = img_arr.reshape(-1, 3) # Reshape to 2D array
    unique_colors, counts = np.unique(pixels, axis=0, return_counts=True)
    sorted_indices = np.argsort(counts)[::-1] # Sort in descending order
    top_colors = unique_colors[sorted_indices][:top_n] # Get top_10 colors
    top_percentages = (counts[sorted_indices][:top_n] / len(pixels)) * 100 # Get top_10 percentages
    return {
        "#{:02x}{:02x}{:02x}".format(*color): round(percentage, 2)
        for color, percentage in zip(top_colors, top_percentages)
    }

# Create a Flask app
app = Flask(__name__) # Create a Flask app
app.secret_key = "your_secret_key"
Bootstrap5(app)  # Initialize Bootstrap

# Configure upload folder
UPLOAD_FOLDER = os.path.join(app.root_path, 'static', 'assets', 'uploads')  # Define upload folder
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Create upload folder if it doesn't exist
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# Flask-WTF Form
class UploadForm(FlaskForm):
    image = FileField("Choose an Image", validators=[DataRequired(message="Please select a file.")])
    submit = SubmitField("Upload IMG")

@app.route("/", methods=["GET", "POST"])
def index():
    form = UploadForm()
    uploaded_image = session.get('uploaded_image')  # Retrieve from session if available
    colors = None

    if form.validate_on_submit():
        # Save uploaded file
        file = form.image.data
        file_name = file.filename  # Get file name
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_name)
        file.save(file_path)

        uploaded_image = f"assets/uploads/{file_name}"  # Path for rendering
        session['file_path'] = file_path  # Save file path in session
        session['uploaded_image'] = uploaded_image  # Save uploaded image path in session
        flash("File uploaded successfully!", "success")

    # Retrieve colors from session if available
    if 'hex_color_dict' in session:
        colors = [
            {"hex": hex_code, "percentage": percentage}
            for hex_code, percentage in session['hex_color_dict'].items()
        ]
        session.pop('hex_color_dict', None)  # Clear colors after rendering

    return render_template("index.html", form=form, uploaded_image=uploaded_image, colors=colors)



@app.route('/extract_color', methods=['POST'])
def extract():
    file_path = session.get('file_path')
    if not file_path or not os.path.exists(file_path):
        flash('No image file found. Please upload an image first.', 'danger')
        return redirect(url_for('index'))  # Redirect to index if no file is found

    # Extract colors
    hex_color_dict = get_top_colors(file_path)
    session['hex_color_dict'] = hex_color_dict  # Store the color data in session
    flash('Color extraction successful!', 'success')
    return redirect(url_for('index'))  # Redirect to index after processing



# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=5000)
