import os
from flask import Blueprint, session, url_for, redirect

bp = Blueprint("logout", __name__, url_prefix='/logout')


@bp.route('', methods=['POST'])
def logout_active_user():
    session.pop('user', default=None)
    return redirect(url_for('home.show_homepage'))
