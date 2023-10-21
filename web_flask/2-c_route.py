#!/usr/bin/python3
"""Import Module"""
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    #start function
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    #start function
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c(text):
    #start function
    s=text.replace('_', ' ')
    return 'C '+ s


if __name__ == '__main__':
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(host='0.0.0.0')