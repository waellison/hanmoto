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
from flask import Blueprint, Response, abort
from flask_admin.contrib.sqla import ModelView
import sqlalchemy
from . import wep_erect, SITE_NAME, admin, wep_make_pagination_links
from ..models import db
from ..models.WEPPost import WEPPost


bp = Blueprint('posts-view', __name__, url_prefix='/posts')


class PostAdminView(ModelView):
    page_size = 10
    column_exclude_list = ['content', 'creation_date', 'last_edit_date', 'slug']


admin.add_view(PostAdminView(WEPPost, db.session, name='Posts', endpoint='posts'))


@bp.route('<int:post_id>', methods=['GET'])
def read_specific_post(post_id: int) -> Response:
    post = WEPPost.query.get_or_404(post_id)
    posts = WEPPost.query.all()
    where = posts.index(post)

    if where != 0:
        prev_page = posts[where - 1].linkify(presigil="&laquo; ")\
                        if posts[where - 1].is_published \
                        else None
    else:
        prev_page = None

    if where != len(posts) - 1:
        next_page = posts[where + 1].linkify(postsigil=" &raquo;")\
                        if posts[where + 1].is_published \
                        else None
    else:
        next_page = None

    if not post.is_published:
        abort(403, "Cannot read unpublished post")

    body_html = list()
    body_html.append(post.html_serialize_name())
    body_html.append(post.html_serialize_author())
    body_html.append(post.html_serialize_content())
    body_html.append("<h4>Categories</h4>\n<ul>")
    body_html.extend([c.listify() for c in post.categories])
    body_html.append("</ul>")

    wep_make_pagination_links(prev_page, next_page, body_html)

    inner_html = "\n".join(body_html)
    output = wep_erect(title=post.name, body_html=inner_html)
    return Response(output, mimetype='text/html')


@bp.route('/all', methods=['GET'])
def list_all_posts() -> Response:
    posts = WEPPost.query.filter_by(is_published=True).order_by(sqlalchemy.desc(WEPPost.publication_date)).all()
    stuff = list()
    stuff.append(f"<h2>Posts on {SITE_NAME}</h2>")
    stuff.append("<ol>")
    stuff.extend([p.listify() for p in posts if p.is_published])
    stuff.append("</ol>")
    post_html = "\n".join(stuff)
    output = wep_erect(title="Posts on this site", body_html=post_html)
    return Response(output, mimetype='text/html')
