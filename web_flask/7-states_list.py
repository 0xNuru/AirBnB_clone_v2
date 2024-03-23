#!/usr/bin/python3
"""A script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    """called automatically at the end of each request"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def get_states():
    """display a list of all states"""
    states = storage.all("State")
    return render_template("7-states_list.html", table="States", states=states)


if __name__ == '__main__':
    # Run Flask app, listening on all available network interfaces on port 5000
    app.run(host='0.0.0.0', port=5000)
