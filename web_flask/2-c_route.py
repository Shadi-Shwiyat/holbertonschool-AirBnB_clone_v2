#!/usr/bin/python3
"""  Script that starts a Flask web application """

from flask import Flask


def start_flask():
    """ Start a Flask web application """
    app = Flask(__name__)

    @app.route('/', strict_slashes=False)
    def hello():
        """ Display 'Hello HBNB!' """
        return 'Hello HBNB!'

    @app.route('/hbnb', strict_slashes=False)
    def hbnb():
        """ Display "HBNB" """
        return 'HBNB'

    @app.route('/c/<text>', strict_slashes=False)
    def c(text):
        """ Display "C" followed by text variable """
        no_underscore = text.replace('_', ' ')
        return f'C {no_underscore}'

    app.run(host='0.0.0.0', port=5000)


if __name__ == "__main__":
    start_flask()
