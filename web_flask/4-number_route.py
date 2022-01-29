#!/usr/bin/python3
"""starts a Flask web application
"""


from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """index domain"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def index2():
    """index domain"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cfun(text):
    """display C followed by the value of the text variable """
    ntext = text.replace('_', ' ')
    return "C {}".format(ntext)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pcool(text="is cool"):
    """display Python, followed by the value of the text variable """
    ptext = text.replace('_', ' ')
    return "Python {}".format(ptext)


@app.route('/number/<n>', strict_slashes=False)
def n_int(n):
    """display Python, followed by the value of the text variable """
    if type(n) is int:
        return "{}is a number".format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
