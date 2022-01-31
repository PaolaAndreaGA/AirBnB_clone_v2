#!/usr/bin/python3
""" Flask web application """
from flask import Flask, render_template
from models import storage
import os

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def list_states_or_cities():
    ''' Page with states '''
    from models.state import State
    from models.city import City
    from models.amenity import Amenity
    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        return render_template('9-states.html', ls_states=State.cities())
    list_states = list(storage.all(State).values())
    list_cities = list(storage.all(City).values())
    list_amenities = list(storage.all(Amenity).values())
    return render_template(
        '10-hbnb_filters.html',
        ls_states=list_states,
        ls_cities=list_cities,
        ls_amenities=list_amenities)


@app.teardown_appcontext
def teardown_x(self):
    ''' Closes session '''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
