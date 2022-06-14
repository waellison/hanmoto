"""Tag-related views for WillPress.

"An Excellent Blog Engine"

Copyright (c) 2021-2022 by William Ellison.  This program is licensed under
the terms of the Do What the Fuck You Want To Public License, version 2
or later, as described in the COPYING file at the root of this
distribution.

William Ellison
<waellison@gmail.com>
"""
from sqlalchemy.exc import SQLAlchemyError
from flask import Blueprint, Response, jsonify, request, abort
from app.models import db
from app.models.WEPTag import WEPTag


bp = Blueprint("tags-view", __name__, url_prefix="/tags")


@bp.route("/<slug>", methods=["GET"])
def read_specific_tag_by_slug(slug: str) -> Response:
    """
    Retrieve a specific tag by its slug.

    Args:
        slug [string]: the slug to try retrieving

    Returns:
        A JSON object representing the found tag, or a
        404 error otherwise.
    """
    tag_id = WEPTag.query.filter_by(slug=slug)[0].id
    return read_specific_tag_json(tag_id)


@bp.route("/<int:tag_id>", methods=["GET"])
def read_specific_tag_json(tag_id: int) -> Response:
    """
    Retrieve a specific slug by its numeric id.

    Args:
        tag_id [int]: the tag ID to retreive

    Returns:
        A JSON object representing the found tag, or a
        404 error otherwise.
    """
    tag = WEPTag.query.get_or_404(tag_id)
    return jsonify(tag.json_serialize())


@bp.route("/all", methods=["GET"])
def list_all_tags():
    """
    Retrieve all tags from within WillPress.

    Returns:
        A JSON object keyed on tag ID with information about every
        tag within WillPress.
    """
    tags = WEPTag.query.order_by(WEPTag.id)

    return jsonify({tag.id: tag.json_serialize() for tag in tags})


@bp.route("/new", methods=["POST"])
def add_new_tag():
    """
    Add a new tag to the system.

    Returns:
        A JSON object representing the tag added to the system,
        if addition was successful; aborts with a 400 error
        otherwise.
    """
    tag = WEPTag(request.form["name"], request.form["summary"])
    try:
        db.session.add(tag)
        db.session.commit()
        return jsonify(tag.json_serialize())
    except SQLAlchemyError as ex:
        abort(400, ex)
