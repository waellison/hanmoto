"""User-related views for WillPress.

"An Excellent Blog Engine"

Copyright (c) 2021-2022 by William Ellison.  This program is licensed under
the terms of the Do What the Fuck You Want To Public License, version 2
or later, as described in the COPYING file at the root of this
distribution.

William Ellison
<waellison@gmail.com>
"""
from sqlalchemy import exc
from flask import Blueprint, Response, request, abort, redirect, url_for, jsonify
from ..models import db
from ..utils import (
    wep_encypher_pw,
    wep_check_all_params_against_set,
    wep_make_gravatar_img,
)
from ..models.WEPUser import WEPUser

bp = Blueprint("users", __name__, url_prefix="/users")


@bp.route("/register", methods=["POST"])
def register_user() -> Response:
    required_params = {"username", "email", "password"}

    missing_params = wep_check_all_params_against_set(required_params, request.form)

    if not missing_params:
        avatar = wep_make_gravatar_img(request.form["email"])
        salt, hashed_pw = wep_encypher_pw(request.form["password"])
        user = WEPUser(
            request.form["username"], hashed_pw, salt, request.form["email"], avatar
        )

        try:
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("home.show_homepage"), code=303)
        except exc.SQLAlchemyError as ex:
            abort(400, ex)


@bp.route("<int:user_id>", methods=["GET"])
def show_user(user_id: int) -> Response:
    user = WEPUser.query.get_or_404(user_id)
    return jsonify(user.json_serialize())
