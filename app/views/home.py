import sqlalchemy
from flask import Blueprint, abort, request, jsonify, Response
from . import BASIC_SCAFFOLD
from ..models.WEPPost import WEPPost


bp = Blueprint('home', __name__, url_prefix='/')


@bp.route('/', methods=['GET'])
def show_homepage():
    posts = WEPPost.query.order_by(sqlalchemy.desc(WEPPost.publication_date)).limit(5)

    for p in posts:
        title_str = f"<h2>{p.name}</h2>"
        summary_html = p.summary.html_serialize()

