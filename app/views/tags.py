"""Tag-related views for WillPress.

"An Excellent Blog Engine"

Copyright (c) 2021-2022 by William Ellison.  This program is licensed under
the terms of the Do What the Fuck You Want To Public License, version 2
or later, as described in the COPYING file at the root of this
distribution.

William Ellison
<waellison@gmail.com>
"""
from datetime import datetime
from sqlalchemy import sql
from sqlalchemy.exc import SQLAlchemyError
from flask import Blueprint, Response, jsonify, request, redirect, url_for, abort
from ..models import db
from ..models.WEPTag import WEPTag


bp = Blueprint('tags-view', __name__, url_prefix='/tags')


@bp.route("/<slug>", methods=['GET'])
def read_specific_tag_by_slug(slug: str) -> Response:
    tag_id = WEPTag.query.filter_by(slug=slug)[0].id
    return read_specific_tag_json(tag_id)


@bp.route('/<int:gag_id>', methods=['GET'])
def read_specific_tag_json(tag_id: int) -> Response:
    tag = WEPTag.query.get_or_404(tag_id)
    return jsonify(tag.json_serialize())


@bp.route('/all', methods=['GET'])
def list_all_tags():
    results = db.session.execute(sql.text("""
        WITH tag_occurrences AS (
            SELECT tag_id, COUNT(*) AS posts_with_tag
            FROM post_tags
            GROUP BY tag_id
        ) SELECT t.id, t.name, tao.posts_with_tag
        FROM tag_occurrences tao
        INNER JOIN tags t
        ON t.id = tao.tag_id
        ORDER BY posts_with_tag DESC;
    """)).fetchall()

    tags = WEPTag.query.order_by(WEPTag.id)

    return jsonify({
        tag.id: tag.json_serialize() for tag in tags
    })


@bp.route('/new', methods=['POST'])
def add_new_category():
    cat = WEPCategory(request.form['name'],
                      request.form['summary'],
                      None)
    try:
        db.session.add(cat)
        db.session.commit()
        return redirect(url_for('home.show_homepage'))
    except SQLAlchemyError as ex:
        abort(400, ex)
