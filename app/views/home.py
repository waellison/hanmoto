"""Homepage views for WillPress.

"An Excellent Blog Engine"

Copyright (c) 2021 by William Ellison.  This program is licensed under
the terms of the Do What the Fuck You Want To Public License, version 2
or later, as described in the COPYING file at the root of this
distribution.

William Ellison
<waellison@gmail.com>
October 2021
"""
import sqlalchemy
from flask import Blueprint, Response
from . import wep_erect, SITE_NAME, POSTS_PER_PAGE
from ..models.WEPPost import WEPPost
from ..utils import wep_ap_date_format


bp = Blueprint('home', __name__, url_prefix='/')


@bp.route('/', methods=['GET'])
def show_homepage() -> Response:
    return show_paginated_page(1)


@bp.route('/<int:page_number>', methods=['GET'])
def show_paginated_page(page_number: int) -> Response:
    posts = WEPPost.query.order_by(sqlalchemy.desc(WEPPost.publication_date))
    body_html = []
    offset = POSTS_PER_PAGE * (page_number - 1)
    my_posts = posts[offset:offset + POSTS_PER_PAGE]

    if page_number == 1:
        prev_page = None
    else:
        prev_page = page_number - 1

    if len(my_posts) != POSTS_PER_PAGE:
        next_page = None
    else:
        next_page = page_number + 1

    for post in my_posts:
        title_str = post.html_serialize_name(level=2)
        summary_html = post.html_serialize_summary()
        body_html.append("<article>")
        body_html.append(title_str)
        body_html.append(f"<p class='post-date'>Posted {wep_ap_date_format(post.publication_date)} by {post.post_author.html_serialize()}</p>")
        body_html.append(summary_html)
        body_html.append(f"<p><a href='/posts/{post.id}'>Read more&hellip;</a></p>")
        post_categories = [c.linkify() for c in post.categories]
        body_html.append(f"Categories: {' &bull; '.join(post_categories)}")
        body_html.append("</article>")

    if prev_page or next_page:
        body_html.append("<p class='pagination-nav'>")

    if prev_page:
        body_html.append(f"<a href='/{prev_page}'>&laquo; Previous</a>")

    if prev_page and next_page:
        body_html.append(" &bull; ")

    if next_page:
        body_html.append(f"<a href='/{next_page}'>Next &raquo;</a>")

    if prev_page or next_page:
        body_html.append("</p>")

    output = wep_erect(title=f"{SITE_NAME}: Home", body_html="\n".join(body_html))
    return Response(output, mimetype='text/html')
