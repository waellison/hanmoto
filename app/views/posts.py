"""Post-related view routes for WillPress.

"An Excellent Blog Engine"

Copyright (c) 2021-2022 by William Ellison.  This program is licensed under
the terms of the Do What the Fuck You Want To Public License, version 2
or later, as described in the COPYING file at the root of this
distribution.

William Ellison
<waellison@gmail.com>
"""
import json
from flask import Blueprint, Response, abort, jsonify
import sqlalchemy
from ..models import db
from ..models.WEPPost import WEPPost


bp = Blueprint("posts-view", __name__, url_prefix="/posts")


@bp.route("<int:post_id>", methods=["GET"])
def read_specific_post(post_id: int) -> Response:
    post = WEPPost.query.get_or_404(post_id)
    posts = (
        WEPPost.query.filter_by(is_published=True)
        .order_by(sqlalchemy.desc(WEPPost.publication_date))
        .all()
    )
    where = posts.index(post)
    prev_post = posts[where - 1].id if where != 0 else None
    next_post = posts[where + 1].id if where != len(posts) - 1 else None

    post_object = post.json_serialize()
    post_object["previous_id"] = prev_post
    post_object["next_id"] = next_post

    if not post.is_published:
        abort(403, "Cannot read unpublished post")

    the_response = jsonify(post_object)
    return the_response


@bp.route("/all", methods=["GET"])
def list_all_posts() -> Response:
    posts = (
        WEPPost.query.filter_by(is_published=True)
        .order_by(sqlalchemy.desc(WEPPost.publication_date))
        .all()
    )
    return jsonify([post.json_serialize() for post in posts])
