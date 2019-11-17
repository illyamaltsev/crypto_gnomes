""" This app module:
    - Create app, connect db, assets and register all Blueprints
    - It is app fabric
    - Each module (see `module` folder) is Blueprint
    - Each module can have
        - controllers.py - here all blueprints routes like `@blueprint_name.routes()`
        - ...
    - Each module can have folder `blueprint_name` in folder `templates` html files are if is wanted.
    - -//- for `static` folder
"""

from flask import Flask

from app.database import models
from app.database.marshmallow import ma


def create_app(config_object=None):
    """ Creating flask app and do all config
    """
    app = Flask(__name__)

    app.config.from_object(config_object)

    """ DB, migration and marshmallow connection
    """
    db = models.db
    db.init_app(app)
    ma.init_app(app)

    """ Blueprints connection
    """
    from app.modules import pages
    from app.modules import api
    from app.modules import auth

    # pages - responses html pages of apb to client
    app.register_blueprint(pages.pages)

    # api - responses json objects from db by AJAX to fill the page
    app.register_blueprint(api.api)

    app.register_blueprint(auth.authBP)

    return app
