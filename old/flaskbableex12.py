from flask import *
from flask_babelex import *

from flask import g, request
from decimal import Decimal
import flask
from datetime import datetime
import flask_babelex as babel
from flask_babelex import gettext, ngettext, lazy_gettext
from flask_babelex._compat import text_type

app = Flask(__name__)
babel = Babel(app)

@babel.localeselector
def get_locale():
    # if a user is logged in, use the locale from the user settings
    user = getattr(g, 'user', None)
    if user is not None:
        print(user.locale)
    # otherwise try to guess the language from the user accept
    # header the browser transmits.  We support de/fr/en in this
    # example.  The best match wins.
    print(request.accept_languages.best_match(['de', 'fr', 'en']))

@babel.timezoneselector

def get_timezone():
    user = getattr(g, 'user', None),request.accept_languages.best_match(['de', 'fr', 'en'])
    if user is not None:
        print(user.timezone)


