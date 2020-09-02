#!/usr/bin/python3
""" starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def index():
    """display the states and cities """
    states = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """close db"""
    storage.close()


if __name__ == '__main__':
    app.run(port='5000', debug=True, host='0.0.0.0')
