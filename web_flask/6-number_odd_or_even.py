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

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
	return "Python {}".format(text.replace('_', ' '))

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
	return "{} is a number".format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
	if isinstance(n, int):
		return render_template('5-number.html', n=n)
	else:
		return abort(404)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
	return render_template("6-number_odd_or_even.html", n=n)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
