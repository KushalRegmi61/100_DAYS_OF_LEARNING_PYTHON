from flask import Flask, request, render_template, redirect, url_for, flash, session
import os
from PIL import Image
import numpy as np

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session and flash messages
UPLOAD_FOLDER = os.path.join(app.root_path, 'static', 'assets', 'uploads') # Define upload folder
os.makedirs(UPLOAD_FOLDER, exist_ok=True) # Create upload folder if it doesn't exist
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Define helper to extract top colors
def get_top_colors(image_path, top_n=10):
    image = Image.open(image_path).convert('RGB')
    img_arr = np.array(image)
    pixels = img_arr.reshape(-1, 3)
    unique_colors, counts = np.unique(pixels, axis=0, return_counts=True)
    sorted_indices = np.argsort(counts)[::-1]
    top_colors = unique_colors[sorted_indices][:top_n]
    top_percentages = (counts[sorted_indices][:top_n] / len(pixels)) * 100
    return {
        "#{:02x}{:02x}{:02x}".format(*color): round(percentage, 2)
        for color, percentage in zip(top_colors, top_percentages)
    }

# Define routes
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if 'image' not in request.files:
            flash('No image file selected!', 'danger')
            return redirect(request.url)
        image_file = request.files['image']
        if image_file and image_file.filename:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], image_file.filename)
            image_file.save(file_path)
            session['hex_color_dict'] = get_top_colors(file_path)
            session['file_path'] = file_path
            flash('Image uploaded and colors extracted successfully!', 'success')
        else:
            flash('Invalid file. Please upload an image.', 'danger')
    hex_color_dict = session.get('hex_color_dict', {})
    return render_template('index.html', hex_color_dict=hex_color_dict)

@app.route('/extract', methods=['POST'])
def extract():
    file_path = session.get('file_path')
    if not file_path or not os.path.exists(file_path):
        flash('No image file found. Please upload an image first.', 'danger')
        return redirect(url_for('home'))
    session['hex_color_dict'] = get_top_colors(file_path)
    flash('Color extraction successful!', 'success')
    return redirect(url_for('home'))

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=5000)
