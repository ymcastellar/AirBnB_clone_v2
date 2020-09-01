#!/usr/bin/python3
""" starts a Flask web application """
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ return page """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def index1():
    """ return page """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def index2(text):
    """ Dynamic Routes """
    name = text.replace("_", " ")
    return 'C {}'.format(name)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def index3(text='is cool'):
    """ Dynamic Routes python """
    name = text.replace("_", " ")
    return 'Python {}'.format(name)


if __name__ == '__main__':
    app.run(port='5000', debug=True, host='0.0.0.0')
