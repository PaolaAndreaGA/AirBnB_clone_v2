#!/usr/bin/python3
"""
starts a Flask web application
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """display"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def index2():
    """display"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cfun(text):
    """pass a data and show the data"""
    new_text = text.replace('_', ' ')
    return "C {}".format(new_text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pcool(text="is cool"):
    """pass a deta ans show the data"""
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def n_int(n):
    """pass a deta ans show the data"""
    if type(n) is int:
        return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def show_tag(n):
    """show a tag html"""
    if isinstance(n, int):
        return render_template('5-number.html', num=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def show_html_tag2(n):
    """show a tag html"""
    if isinstance(n, int):
        if n % 2 == 0:
            strg = "even"
        else:
            strg = "odd"
        return render_template('6-number_odd_or_even.html', num=n, ev_od=strg)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
