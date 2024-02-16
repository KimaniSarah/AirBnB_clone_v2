#!/usr/bin/python3
"""Write a script that starts a Flask web application:"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def display_hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    return "HBNB"


@app.route("//c/<text>", strict_slashes=False)
def display_c(text):
    string = text.replace('_', ' ')
    return f"C {string}"


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python", strict_slashes=False)
def display_python(text="is_cool"):
    string = text.replace('_', ' ')
    return f"Python {string}"


@app.route("/number/<int:n>", strict_slashes=False)
@app.route("/number", strict_slashes=False)
def display_num(n=None):
    if n is not None and isinstance(n, int):
        return f"{n} is a number"
    else:
        return f"{n} is not a number"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
