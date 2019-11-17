""" This module:
    - handle all AJAX requests from apb and receipt pages
"""


from flask import Blueprint

api = Blueprint('api', __name__)

from . import controllers
