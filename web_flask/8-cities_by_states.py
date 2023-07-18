#!/usr/bin/python3
"""  Script that starts a Flask web application """

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_and_states():
    ''' Display all cities by states '''
    city_list = storage.all(State)
    return render_template('8-cities_by_states.html', city_list=city_list)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
