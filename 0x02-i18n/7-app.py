#!/usr/bin/env python3

"""
This module creates an instance of Flask application and
defines a class and welcome_message function.
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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

    # Locale from user settings
    if g.user:
        locale = g.user.get('locale')
        if locale and locale in app.config['LANGUAGES']:
            return locale

    # Locale from request header
    locale = request.headers.get('locale', None)
    if locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


# babel.init_app(app, locale_selector=get_locale)


def get_user():
    """
    Returns a user dictionary or None if the ID cannot
    be found or if login_as was not passed.
    """
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request():
    """
    Executed before all other functions.
    """
    g.user = get_user()


@babel.timezoneselector
def get_timezone():
    """
    Select and return appropriate timezone
    """
    # Find timezone parameter in URL parameters
    tzone = request.args.get('timezone', None)
    if tzone:
        try:
            return timezone(tzone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    # Find time zone from user settings
    if g.user:
        try:
            tzone = g.user.get('timezone')
            return timezone(tzone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    # Default to UTC
    default_tz = app.config['BABEL_DEFAULT_TIMEZONE']
    return default_tz


@app.route('/')
def welcome_message() -> str:
    """
    Displays a welcome message on the homepage.

    Returns:
            str: Rendered HTML template with the welcome message.
    """
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run()
