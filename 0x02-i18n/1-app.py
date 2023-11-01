#!/usr/bin/env python3

"""
This module creates an instance of Flask application and
defines a class and welcome_message function.
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """Configuration class for Flask app."""
    LANGUAGES = ["en", "fr"]  # Available languages for the app
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)

# Use the Config class as the config for the Flask app
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@app.route('/')
def welcome_message() -> str:
    """
    Displays a welcome message on the homepage.

    Returns:
            str: Rendered HTML template with the welcome message.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
