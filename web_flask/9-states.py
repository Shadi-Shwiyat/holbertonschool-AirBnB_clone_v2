#!/usr/bin/python3
''' Start a Flask web aplication '''
from flask import Flask, abort, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states/')
@app.route('/states/<state_id>')
def states(state_id=None):
    ''' Display states and state '''
    states = storage.all(State)
    if state_id is not None:
        state_id = 'State.' + state_id
    return render_template('9-states.html', states=states, state_id=state_id)


@app.teardown_appcontext
def do_teardown(self):
    ''' Remove the current SQLAlchemy Session '''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)