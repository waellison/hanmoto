"""User-related views for WillPress.

"An Excellent Blog Engine"

Copyright (c) 2021-2022 by William Ellison.  This program is licensed under
the terms of the Do What the Fuck You Want To Public License, version 2
or later, as described in the COPYING file at the root of this
distribution.

William Ellison
<waellison@gmail.com>
"""
from flask import Blueprint, Response, request, abort, redirect, session, url_for
from . import SITE_NAME
from ..utils import wep_encypher_pw, wep_check_all_params_against_set
from ..models.WEPUser import WEPUser

bp = Blueprint("login", __name__, url_prefix="/login")


@bp.route("", methods=["POST"])
def do_login():
    if request.method == "POST":
        required_params = {"username", "password"}

        missing_params = wep_check_all_params_against_set(required_params, request.form)

        if not missing_params:
            username = request.form["username"]
            user = WEPUser.query.filter_by(username=username).first()

            if user:
                _, hashed_pw = wep_encypher_pw(request.form["password"], salt=user.salt)
                if hashed_pw == user.password:
                    session["user"] = user.json_serialize()
                    return redirect(url_for("home.show_homepage"), code=303)
                else:
                    abort(403)
            else:
                abort(401)
        else:
            abort(400)
