"""Error-related view routes for WillPress.

"An Excellent Blog Engine"

Copyright (c) 2021-2022 by William Ellison.  This program is licensed under
the terms of the Do What the Fuck You Want To Public License, version 2
or later, as described in the COPYING file at the root of this
distribution.

William Ellison
<waellison@gmail.com>
"""
from flask import Blueprint, Response, jsonify
from werkzeug.exceptions import HTTPException

bp = Blueprint("errors", __name__)


@bp.app_errorhandler(HTTPException)
def handle_error(err: HTTPException) -> Response:
    """
    Gracefully handle all errors raised by the web server.

    Args:
        err [werkzeug.exceptions.HTTPException]: The error raised by the Web server.

    Returns:
        A JSON object describing the raised error.
    """
    return jsonify(
        {
            "error_code": err.code,
            "error_description": err.description,
        }
    )
