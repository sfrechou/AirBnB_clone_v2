#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models import State
app = Flask(
    __name__,
    template_folder="templates"
)
app.url_map.strict_slashes = False


@app.route('/states')
def states():
    """display a HTML page"""
    new_dict = storage.all(State)
    return render_template('9-states.html', states=new_dict)


@app.route('/states/<id>')
def states_id(id):
    """display a HTML page"""
    new_dict = storage.all(State)
    if "State." + id in new_dict:
        for key, value in new_dict.items():
            if id in key:
                name = value.name
                city_dict = value.cities
    else:
        return render_template('9-states.html', els=True)
    return render_template('9-states.html', cities=city_dict,
                           id=id, name=name)


@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
