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
from flask import Blueprint, Response, abort, jsonify
import sqlalchemy
from ..models import db
from ..models.WEPPost import WEPPost


bp = Blueprint('posts-view', __name__, url_prefix='/posts')


@bp.route('<int:post_id>', methods=['GET'])
def read_specific_post(post_id: int) -> Response:
    post = WEPPost.query.get_or_404(post_id)
    posts = WEPPost.query.all()
    where = posts.index(post)

    if not post.is_published:
        abort(403, "Cannot read unpublished post")

    return jsonify(post.json_serialize())


@bp.route('/all', methods=['GET'])
def list_all_posts() -> Response:
    posts = WEPPost.query.filter_by(is_published=True)\
                         .order_by(sqlalchemy.desc(WEPPost.publication_date)).all()
    return jsonify([post.json_serialize() for post in posts])
