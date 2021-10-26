from sqlalchemy import and_, sql
from flask import Blueprint, Response, request, abort, redirect, session, url_for
from ..utils import wep_encypher_pw, wep_check_all_params_against_set
from ..models import db
from ..models.WEPUser import WEPUser

bp = Blueprint("login", __name__, url_prefix='/login')


@bp.route('', methods=['GET'])
def show_login():
    return Response("fack", mimetype='text/html')


@bp.route('', methods=['POST'])
def try_login():
    required_params = {
        "username",
        "password"
    }

    missing_params = wep_check_all_params_against_set(required_params, request.form)

    if not missing_params:
        username = request.form['username']
        user = WEPUser.query.filter_by(username=username).first()

        if user:
            _, hashed_pw = wep_encypher_pw(request.form['password'], salt=user.salt)
            if hashed_pw == user.password:
                session['user'] = user.json_serialize()
                return redirect(url_for('home.show_homepage'), code=303)
            else:
                abort(403)
        else:
            abort(401)
    else:
        abort(400)