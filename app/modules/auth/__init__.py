""" This module:
    - handle authenticate in APB
"""


from functools import wraps

from flask import Blueprint
from flask import session, redirect, url_for

authBP = Blueprint('auth', __name__, template_folder='templates/auth',
                   static_folder='static', static_url_path='/../static/apb')

from . import controllers


def login_required(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        if session and session['user_id']:
            return f(*args, **kwargs)
        else:
            return redirect(url_for("pages.login"))
    return wrapped
