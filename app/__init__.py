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
from flask_admin.contrib.appengine import ModelView

from app.database import models
from app.database.marshmallow import ma
from flask_admin import Admin

from app.database.models import User, Coin, UserCoin


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

    # set optional bootswatch theme
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

    admin = Admin(app, name='admin', template_mode='bootstrap3')
    #admin.add_view(ModelView(Coin, db.session))
    #admin.add_view(ModelView(UserCoin, db.session))
    # Add administrative views here

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
