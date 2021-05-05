#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models import State, Amenity
app = Flask(
    __name__,
    template_folder="templates"
)
app.url_map.strict_slashes = False


@app.route('/hbnb_filters')
def hbnb_filters():
    """display a HTML page"""
    state_dict = storage.all(State)
    amen_dict = storage.all(Amenity)
    return render_template('10-hbnb_filters.html', states=state_dict, amens = amen_dict)


@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
