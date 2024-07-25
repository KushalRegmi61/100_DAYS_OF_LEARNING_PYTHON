"""This just a basic version of the Higher_lower game. Will modify it more in future."""
from flask import Flask
import random


#Gif links
high='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'
low='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'
correct='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'


CORRECT_NUMBER=None
#method to generate a random number 
def random_number():
    global CORRECT_NUMBER
    CORRECT_NUMBER=random.randint(0,9)
    
random_number()    



app = Flask(__name__)

@app.route("/")
def home():
    return (
        f"<div style='text-align: center'>"
        f"<h1 style='color: Red'>Guess a number between 0 and 9</h1>"
        f"<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"
        f"</div>"
    )

@app.route("/<int:guess_number>")
def check_number(guess_number):
    if CORRECT_NUMBER>guess_number:
        return (
            f"<div style='text-align: center'>"
            f"<h1 style='color: Red'>Too low, Try again.</h1>"
            f"<img src={low}>"
            f"</div>"
        )
    elif CORRECT_NUMBER<guess_number:
        return (
            f"<div style='text-align: center'>"
            f"<h1 style='color: Red'>Too High, Try again.</h1>"
            f"<img src={high}>"
            f"</div>"
        )
    else: 
        return (
            f"<div style='text-align: center'>"
            f"<h1 style='color: Red'>You Found me.</h1>"
            f"<img src={correct}>"
            f"</div>"
        )


if __name__=="__main__":
    app.run(host='localhost', port=8000, debug=True)