#!/usr/bin/env python3

"""
This module creates an instance of Flask application and
defines welcome_message function.
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def welcome_message() -> str:
    """
    Displays a welcome message on the homepage.

    Returns:
            str: Rendered HTML template with the welcome message.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
