#!/usr/bin/python3
""" Script that starts a Flask web application
at 0.0.0.0:5000

Routes:
	'/' and '/hbnb' display "Hellow HBNB!"
"""
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_route():
	""" Prints the text 'Hello BNBN!"""
	return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
	"""prints Hello HBNB"""
	return "HBNB!"

@app.route('/c/<text>', strict_slashes=False)
def c_isFun(text):
	"""Prints the letter "C" follow by <text> """
	return "C {}".format(text.replace('_', ' '))

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)

