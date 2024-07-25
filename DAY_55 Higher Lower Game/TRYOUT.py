from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper_function():
        return f"<b>{function()}</b>"
    return wrapper_function

def make_emphasis(function):
    def wrapper_function():
        return f"<em>{function()}</em>"
    return wrapper_function    

def underline(function):
    def wrapper_function():
        return f"<u>{function()}</u>"
    return wrapper_function

@app.route("/")
@make_bold
@make_emphasis
@underline
def hello():
    return (f"<div style='text-align: center'>"
            f"<h1>Hello, World</h1>"
            f"<img src='https://media.giphy.com/media/QydOVgahElhEYVih6Q/giphy.gif' width='200'>"
            f"</div>"
    )

@app.route("/bye/<username>/<int:age>")
def bye(username, age):
    return f"Bye! {username}, Age: {age}."

if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)
