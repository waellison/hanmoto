"""
Application initialization logic for WillPress.

"An Excellent Blog Engine"

Copyright (c) 2021 by William Ellison.  This program is licensed under
the terms of the Do What the Fuck You Want To Public License, version 2
or later, as described in the COPYING file at the root of this
distribution.

William Ellison
<waellison@gmail.com>
October 2021
"""
import os
from flask import Flask
from flask_migrate import Migrate
from .models import db
from .views import categories, posts, home, login, logout


def wep_create_app(test_config=None):
    """Create and return a new Flask app."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=os.getenv('secret_key'),
        SQLALCHEMY_DATABASE_URI='postgresql://postgres@localhost:5432/willpress',
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SQLALCHEMY_ECHO=True
    )

    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.app = app
    db.init_app(app)
    db.create_all()
    _ = Migrate(app, db)

    app.register_blueprint(posts.bp)
    app.register_blueprint(categories.bp)
    app.register_blueprint(home.bp)
    app.register_blueprint(login.bp)
    app.register_blueprint(logout.bp)

    return app
