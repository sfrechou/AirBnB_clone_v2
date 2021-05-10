#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models import State, Amenity, Place, User
app = Flask(
    __name__,
    template_folder="templates"
)
app.url_map.strict_slashes = False


@app.route('/hbnb')
def hbnb():
    """display a HTML page"""
    state_dict = storage.all(State)
    amen_dict = storage.all(Amenity)
    all_places = storage.all(Place)
    users = storage.all(User)
    return render_template('100-hbnb.html', states=state_dict, amens = amen_dict, places=all_places, users=users)


@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
