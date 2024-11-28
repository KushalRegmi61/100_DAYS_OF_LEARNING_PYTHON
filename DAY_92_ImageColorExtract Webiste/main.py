from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__) # Create an instance of the Flask class

#Global variables

HEX_COLOR_DICT = {}



# Home page
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get the hold of the image file
        image_file = request.files['image-file']
        # Access the image file (e.g., save it to a directory)
        image_file.save(f'./uploads/{image_file.filename}')


    return render_template('index.html')



# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=5000)