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
import dotenv
from flask import Flask
from flask_migrate import Migrate
from .models import db
from .views import admin, categories, posts, home, users, login, logout


def wep_create_app(test_config=True):
    """Create and return a new Flask app."""
    dotenv.load_dotenv("..")
    app = Flask(__name__, instance_relative_config=True)

    if test_config:
        app.config.from_mapping(
            SECRET_KEY=os.getenv("secret_key"),
            SQLALCHEMY_DATABASE_URI="postgresql://postgres:hunter2@pg:5432/uchapishaji",
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
            SQLALCHEMY_ECHO=False,
        )
    else:
        app.config.from_mapping(
            SECRET_KEY=os.getenv("secret_key"),
            SQLALCHEMY_DATABASE_URI="postgresql://postgres@pg:5432/uchapishaji",
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
            SQLALCHEMY_ECHO=True,
        )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.app = app
    db.init_app(app)
    db.create_all()
    _ = Migrate(app, db)

    admin.app = app
    admin.init_app(app)

    app.register_blueprint(posts.bp)
    app.register_blueprint(categories.bp)
    app.register_blueprint(home.bp)
    app.register_blueprint(login.bp)
    app.register_blueprint(logout.bp)
    app.register_blueprint(users.bp)

    return app
