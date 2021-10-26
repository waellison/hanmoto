"""Post-related view routes for WillPress.

"An Excellent Blog Engine"

Copyright (c) 2021 by William Ellison.  This program is licensed under
the terms of the Do What the Fuck You Want To Public License, version 2
or later, as described in the COPYING file at the root of this
distribution.

William Ellison
<waellison@gmail.com>
October 2021
"""
from flask import Blueprint, Response
import sqlalchemy
from ..utils import wep_ap_date_format
from . import wep_erect, SITE_NAME
from ..models.WEPPost import WEPPost


bp = Blueprint('posts', __name__, url_prefix='/posts')


@bp.route('<int:post_id>', methods=['GET'])
def read_specific_post(post_id: int) -> Response:
    post = WEPPost.query.get_or_404(post_id)
    body_html = list()
    body_html.append(post.html_serialize_name())
    body_html.append(post.html_serialize_author())
#    body_html.append(f"<p>Published on {wep_ap_date_format(post.publication_date)}</p>")
    body_html.append(post.html_serialize_content())
    body_html.append("<h4>Categories</h4>\n<ol>")
    body_html.extend([c.listify() for c in post.categories])
    body_html.append("</ol>")
    inner_html = "\n".join(body_html)
    output = wep_erect(title=post.name, body_html=inner_html)
    return Response(output, mimetype='text/html')


@bp.route('/all', methods=['GET'])
def list_all_posts() -> Response:
    posts = WEPPost.query.order_by(sqlalchemy.desc(WEPPost.publication_date)).all()
    stuff = list()
    stuff.append(f"<h2>Posts on {SITE_NAME}</h2>")
    stuff.append("<ol>")
    stuff.extend([p.listify() for p in posts])
    stuff.append("</ol>")
    post_html = "\n".join(stuff)
    output = wep_erect(title="Posts on this site", body_html=post_html)
    return Response(output, mimetype='text/html')
