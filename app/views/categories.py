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
from flask import Blueprint, Response
from . import wep_erect, SITE_NAME
from ..models import db
from ..models.WEPCategory import WEPCategory


bp = Blueprint('categories', __name__, url_prefix='/categories')


@bp.route('/<int:cat_id>/json', methods=['GET'])
def read_specific_category_json(cat_id: int) -> Response:
    category = WEPCategory.query.get_or_404(cat_id)
    return jsonify(category.json_serialize())


@bp.route('/<int:cat_id>', methods=['GET'])
def read_specific_category(cat_id: int) -> Response:
    category = WEPCategory.query.get_or_404(cat_id)
    body_html = list()
    body_html.append(f"<h2>Posts in category <em>{category.name}</em></h2>")
    body_html.append(category.html_serialize_summary())
    body_html.append("<ul>")
    body_html.extend([p.listify() for p in category.associated_posts])
    body_html.append("</ul>")
    inner_html = "\n".join(body_html)
    output = wep_erect(title=category.name, body_html=inner_html)
    return Response(output, mimetype='text/html')


@bp.route('/all', methods=['GET'])
def list_all_categories():
    results = db.session.execute("""
        WITH category_occurrences AS (
            SELECT category_id, COUNT(*) AS posts_in_category
            FROM post_categories
            GROUP BY category_id
        ) SELECT c.id, c.name, co.posts_in_category
        FROM category_occurrences co
        INNER JOIN categories c
        ON c.id = co.category_id
        ORDER BY posts_in_category DESC;
    """)

    body_html = list()
    body_html.append(f"<h2>Categories on {SITE_NAME}</h2>")
    body_html.append("<ul>")

    for result in results:
        category_id = result[0]
        c = WEPCategory.query.get_or_404(category_id)
        body_html.append(c.listify())

    body_html.append("</ul>")
    inner_html = "\n".join(body_html)
    output = wep_erect(title="Categories on this site", body_html=inner_html)
    return Response(output, mimetype='text/html')
