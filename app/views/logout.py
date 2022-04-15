"""Logout-related views for WillPress.

"An Excellent Blog Engine"

Copyright (c) 2021-2022 by William Ellison.  This program is licensed under
the terms of the Do What the Fuck You Want To Public License, version 2
or later, as described in the COPYING file at the root of this
distribution.

William Ellison
<waellison@gmail.com>
"""
from flask import Blueprint, session

bp = Blueprint("logout", __name__, url_prefix='/logout')


@bp.route('', methods=['GET', 'POST'])
def logout_active_user():
    session.pop('user', default=None)
    return None
