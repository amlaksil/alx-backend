#!/usr/bin/env python3

"""
This module creates an instance of Flask application and
defines a class and welcome_message function.
"""
from flask import Flask, render_template, request
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


@babel.localeselector
def get_locale() -> str:
    """
    Determine the best-matching language for the user.

    Returns:
            str: Best-matching language code.
    """
    if 'locale' in request.args:
        locale = request.args.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


# babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def welcome_message() -> str:
    """
    Displays a welcome message on the homepage.

    Returns:
            str: Rendered HTML template with the welcome message.
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()
