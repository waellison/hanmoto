import os
from ..utils import env
from flask import redirect, url_for


def show_login():
    return redirect(url_for('google.login'))
