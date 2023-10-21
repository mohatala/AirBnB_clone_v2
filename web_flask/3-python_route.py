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

@app.route('/python', strict_slashes=False)
def python(text= 'is_cool'):
    #start function
    s=text.replace('_', ' ')
    return 'Python '+ s

@app.route('/python/<text>', strict_slashes=False)
def python1(text= 'is_cool'):
    #start function
    s=text.replace('_', ' ')
    return 'Python '+ s


if __name__ == '__main__':
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(host='0.0.0.0')