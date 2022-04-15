"""Homepage views for WillPress.

"An Excellent Blog Engine"

Copyright (c) 2021 by William Ellison.  This program is licensed under
the terms of the Do What the Fuck You Want To Public License, version 2
or later, as described in the COPYING file at the root of this
distribution.

William Ellison
<waellison@gmail.com>
October 2021
"""
from flask import Blueprint, Response, jsonify

from app.views import SITE_NAME

bp = Blueprint('home', __name__, url_prefix='/')


@bp.route('/', methods=['GET'])
def show_homepage() -> Response:
    return jsonify({
        "alive": True
    })


@bp.route('/title', methods=["GET"])
def get_site_name() -> Response:
    return jsonify({
        "siteName": SITE_NAME
    })
