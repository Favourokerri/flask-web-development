#!/usr/bin/python3
""" app instance and application server """
from flask import Flask

app = Flask(__name__)

if __name__ = '__main__':
    app.run(debug=True)
