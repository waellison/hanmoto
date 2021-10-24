from flask import Blueprint, abort, request, Response
import sqlalchemy
from .. import wep_ap_date_format
from . import BASIC_SCAFFOLD
from ..models import db
from ..models.WEPPost import WEPPost


bp = Blueprint('posts', __name__, url_prefix='/posts')


@bp.route('<int:post_id>', methods=['GET'])
def read_specific_post(post_id: int) -> Response:
    post = WEPPost.query.get_or_404(post_id)
    body_html = list()
    body_html.append(post.html_serialize_name())
    body_html.append(f"Published on {wep_ap_date_format(post.publication_date)}")
    body_html.append(post.html_serialize_content())
    body_html.append("<h3>Categories</h3>\n<ol>")
    body_html.extend([c.listify() for c in post.categories])
    body_html.append("</ol>")
    inner_html = "\n".join(body_html)
    output = BASIC_SCAFFOLD.format(title=post.name, body_html=inner_html)
    return Response(output, mimetype='text/html')


@bp.route('/all', methods=['GET'])
def list_all_posts() -> Response:
    posts = WEPPost.query.order_by(sqlalchemy.desc(WEPPost.publication_date)).all()
    stuff = list()
    stuff.append("<h1>Posts on this site</h1>")
    stuff.append("<ol>")
    stuff.extend([p.listify() for p in posts])
    stuff.append("</ol>")
    post_html = "\n".join(stuff)
    output = BASIC_SCAFFOLD.format(title="Posts on this site", body_html=post_html)
    return Response(output, mimetype='text/html')
