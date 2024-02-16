#!/usr/bin/python3
"""Write a script that starts a Flask web application:"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def display_hello():
    """Display Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """Display HBNB"""
    return "HBNB"


@app.route("//c/<text>", strict_slashes=False)
def display_c(text):
    """Display 'C ' followed by the value of the text variable"""
    string = text.replace('_', ' ')
    return f"C {string}"


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python", strict_slashes=False)
def display_python(text="is_cool"):
    """Display Python + value of the text"""
    string = text.replace('_', ' ')
    return f"Python {string}"


@app.route("/number/<int:n>", strict_slashes=False)
def display_num(n):
    """Display render HTML page if n is an integer"""
    if isinstance(n, int):
        return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def display_html(n):
    """Display render HTML page if n is an integer"""
    if isinstance(n, int):
        return render_template("5-number.html", num=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    """Display render HTML page if n is an odd|even"""
    if isinstance(n, int):
        return render_template("6-number_odd_or_even.html", num=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
