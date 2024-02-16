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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
