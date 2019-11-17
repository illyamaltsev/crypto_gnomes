""" This module:
    - response all pages that client need
"""


from flask import Blueprint

pages = Blueprint('pages', __name__)

from . import controllers
