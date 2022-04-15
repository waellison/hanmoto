"""Category-related views for WillPress.

"An Excellent Blog Engine"

Copyright (c) 2021 by William Ellison.  This program is licensed under
the terms of the Do What the Fuck You Want To Public License, version 2
or later, as described in the COPYING file at the root of this
distribution.

William Ellison
<waellison@gmail.com>
October 2021
"""
from datetime import datetime
from sqlalchemy import sql
from sqlalchemy.exc import SQLAlchemyError
from flask import Blueprint, Response, jsonify, request, redirect, url_for, abort
from ..models import db
from ..models.WEPCategory import WEPCategory


bp = Blueprint("categories-view", __name__, url_prefix="/categories")


@bp.route("/<slug>", methods=["GET"])
def read_specific_category_by_slug(slug: str) -> Response:
    category_id = WEPCategory.query.filter_by(slug=slug)[0].id
    return read_specific_category_json(category_id)


@bp.route("/<int:cat_id>", methods=["GET"])
def read_specific_category_json(cat_id: int) -> Response:
    category = WEPCategory.query.get_or_404(cat_id)
    return jsonify(category.json_serialize())


@bp.route("/all", methods=["GET"])
def list_all_categories():
    results = db.session.execute(
        sql.text(
            """
        WITH category_occurrences AS (
            SELECT category_id, COUNT(*) AS posts_in_category
            FROM post_categories
            GROUP BY category_id
        ) SELECT c.id, c.name, co.posts_in_category
        FROM category_occurrences co
        INNER JOIN categories c
        ON c.id = co.category_id
        ORDER BY posts_in_category DESC;
    """
        )
    ).fetchall()

    categories = WEPCategory.query.order_by(WEPCategory.id)

    return jsonify({cat.id: cat.json_serialize() for cat in categories})


@bp.route("/new", methods=["POST"])
def add_new_category():
    cat = WEPCategory(request.form["name"], request.form["summary"], None)
    try:
        db.session.add(cat)
        db.session.commit()
        return redirect(url_for("home.show_homepage"))
    except SQLAlchemyError as ex:
        abort(400, ex)
