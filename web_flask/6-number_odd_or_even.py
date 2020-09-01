#!/usr/bin/python3
""" starts a Flask web application """
from flask import Flask, render_template

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


@app.route('/number/<int:n>', strict_slashes=False)
def index4(n):
    """ Dynamic Routes python """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def index5(n):
    """ Dynamic Routes python """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def index6(n):
    """ Dynamic Routes python """
    if (n % 2) == 0:
        text = 'even'
    else:
        text = 'odd'
    return render_template('6-number_odd_or_even.html', n=n, text=text)


if __name__ == '__main__':
    app.run(port='5000', debug=True, host='0.0.0.0')
