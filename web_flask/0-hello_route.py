#!/usr/bin/python3
""" Script that starts a Flask web application
at 0.0.0.0:5000
"""
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slaches=False)
def hello_route():
	""" Prints the text 'Hello BNBN!"""
	return "Hello HBNB!"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
