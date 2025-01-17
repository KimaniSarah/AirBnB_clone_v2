#!/usr/bin/python3
"""starts a web application"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """remove the current SQLAlchemy Session"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """display a HTML page"""
    objects = storage.all(State).values()
    obj = sorted(objects, key=lambda objects: objects.name)
    return render_template("7-states_list.html", states=obj)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
