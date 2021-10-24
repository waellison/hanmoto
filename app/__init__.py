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
from datetime import datetime
from flask import Flask
from flask_migrate import Migrate
from . import models
from . import views


def wep_ap_date_format(date: datetime) -> str:
    abbreviations = {
        "months": [
            "Jan.",
            "Feb.",
            "March",
            "April",
            "May",
            "June",
            "July",
            "Aug.",
            "Sept.",
            "Oct.",
            "Nov.",
            "Dec."
        ]
    }
    day = date.day
    month = abbreviations["months"][date.month - 1]
    year = date.year
    return f"{month} {day}, {year}"



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
    except OSError:
        pass

    from .models import db
    db.app = app
    db.init_app(app)
    db.create_all()
    _ = Migrate(app, db)

    from .views import posts, categories
    app.register_blueprint(posts.bp)
    app.register_blueprint(categories.bp)

    return app
