import os
from ..utils import env
from flask import redirect, url_for
from flask_dance.contrib.google import make_google_blueprint
from dotenv import load_dotenv

load_dotenv("../..")

bp = make_google_blueprint(
    client_id=os.getenv('GOOGLE_CLIENT_ID'),
    client_secret=os.getenv('GOOGLE_CLIENT_SECRET'),
    reprompt_consent=True,
    scope=['profile', 'email'],
)
bp.name = 'logout'


@bp.route('/logout')
def logout_active_user():
    return redirect(url_for('logout.logout'))
