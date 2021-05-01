#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """display “Hello HBNB!”"""
    return 'Hello HBNB!'

@app.route('/hbnb')
def hbnb():
    """display “HBNB”"""
    return 'HBNB'

@app.route('/c/<text>')
def c_is_fun(text):
    """ display “C ” followed by the value of text"""
    rep = text.replace('_', ' ')
    return 'C {}'.format(rep)

@app.route('/python')
@app.route('/python/<text>')
def python_is_cool(text='is cool'):
    """display “Python ”, followed by the value of text"""
    rep = text.replace('_', ' ')
    return 'Python {}'.format(rep)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
