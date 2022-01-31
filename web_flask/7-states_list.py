#!/usr/bin/python3
""" Basic Flask App with a second subdomain """
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def teardown_data(self):
    """ update data from source """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ /states_list path"""
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
