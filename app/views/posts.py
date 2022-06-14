"""Post-related view routes for WillPress.

"An Excellent Blog Engine"

Copyright (c) 2021-2022 by William Ellison.  This program is licensed under
the terms of the Do What the Fuck You Want To Public License, version 2
or later, as described in the COPYING file at the root of this
distribution.

William Ellison
<waellison@gmail.com>
"""
from flask import Blueprint, Response, abort, jsonify
import sqlalchemy
from ..models.WEPPost import WEPPost
from . import POSTS_PER_PAGE


bp = Blueprint("posts-view", __name__, url_prefix="/posts")


@bp.route("<int:post_id>", methods=["GET"])
def retrieve_specific_post_by_id(post_id: int) -> Response:
    """
    Retrieve a specific post by its id.

    Args:
        post_id [int]: The id of the post we wish to retrieve.

    Returns:
        A JSON object containing the retrieved post
        HTTP 404 if post not found
        HTTP 403 if post not published
    """
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


@bp.route("<slug>", methods=["GET"])
def retrieve_specific_post_by_slug(slug: str) -> Response:
    """
    Retrieve a specific post by its slug.

    A slug is a spinal-case string generated at creation from the post
    title.

    Args:
        slug [str]: The slug of the post we wish to retrieve.

    Returns:
        A JSON object containing the retrieved post
        HTTP 404 if post not found
        HTTP 403 if post not published
    """
    post = WEPPost.query.filter_by(slug=slug).first()

    if post:
        return retrieve_specific_post_by_id(post.id)
    abort(404)


@bp.route("/all", methods=["GET"])
def list_all_posts() -> Response:
    """
    Retrieve all posts within a WillPress site.

    Returns:
        A JSON object containing every published post within
        WillPress.
    """
    posts = (
        WEPPost.query.filter_by(is_published=True)
        .order_by(sqlalchemy.desc(WEPPost.publication_date))
        .all()
    )
    return jsonify([post.json_serialize() for post in posts])


@bp.route("/most-recent", methods=["GET"])
def get_most_recent_posts() -> Response:
    posts = (
        WEPPost.query.filter_by(is_published=True)
        .order_by(sqlalchemy.desc(WEPPost.publication_date))
        .limit(POSTS_PER_PAGE)
    )

    return jsonify([p.json_serialize() for p in posts])


@bp.route("/page/<int:page_number>", methods=["GET"])
def get_paginated_posts(page_number: int) -> Response:
    all_posts = WEPPost.query.filter_by(is_published=True).order_by(
        sqlalchemy.desc(WEPPost.publication_date)
    )
    this_page = slice(
        page_number * POSTS_PER_PAGE, (page_number * POSTS_PER_PAGE) + POSTS_PER_PAGE
    )
    pages = 0
    if all_posts.count() % POSTS_PER_PAGE == 0:
        pages = all_posts.count() // POSTS_PER_PAGE
    else:
        pages = (all_posts.count() // POSTS_PER_PAGE) + 1

    return jsonify(
        {
            "posts": [p.json_serialize() for p in all_posts[this_page]],
            "page": page_number,
            "pageCount": pages,
        }
    )


@bp.route("/post", methods=["POST"])
def add_new_post() -> Response:
    pass
