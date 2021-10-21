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
import sys
import pkgutil
import importlib
from flask import Flask, Blueprint
from flask_migrate import Migrate
from .models import *
from .views import *

def _register_blueprints(app, package_name, package_path):
    """
    Register all blueprint instances on the specified Flask application
    found in all modules for the specified package.
    
    H/T to Github user mattupstate, link:
    https://gist.github.com/mattupstate/5859194

    Args:
    - app: the Flask application instance
    - package_name: the package name
    - package_path: the package path
    """
    rv = []
    
    for _, name, _ in pkgutil.iter_modules(package_path):
        m = importlib.import_module(f"{package_name}.{name}")
        for item in dir(m):
            item = getattr(m, item)
            if isinstance(item, Blueprint):
                app.register_blueprint(item)
            rv.append(item)

    return rv


def wep_create_app(test_config=None):
    """Create and return a new Flask app."""

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI='postgresql://postgres@localhost:5432/willpress',
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SQLALCHEMY_ECHO=True
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError as ex:
        print("wep_create_app: failed to create instance directories")
        print(f"Python reports this error: {ex}")
        sys.exit(1)

    from .models import db
    db.app = app
    db.init_app(app)
    db.create_all()
    _ = Migrate(app, db)

    enregistered_models = register_blueprints(app, "models", ".")
    enregistered_views = register_blueprints(app, "views", ".")

    return app

