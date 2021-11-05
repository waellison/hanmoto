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
from flask import Blueprint, Response, jsonify, session, request, redirect, url_for, abort
from flask_admin.contrib.sqla import ModelView
from . import wep_erect, SITE_NAME, admin
from ..models import db
from ..models.WEPCategory import WEPCategory


bp = Blueprint('categories-view', __name__, url_prefix='/categories')


class CategoryView(ModelView):
    page_size = 10
    column_list = ('name', 'summary', 'parent_category', 'associated_posts')

    column_exclude_list = ['summary', 'slug']
    form_excluded_columns = ['slug']


admin.add_view(CategoryView(WEPCategory, db.session, name='Categories', endpoint='categories'))


@bp.route('/<int:cat_id>/json', methods=['GET'])
def read_specific_category_json(cat_id: int) -> Response:
    category = WEPCategory.query.get_or_404(cat_id)
    return jsonify(category.json_serialize())


@bp.route('/<int:cat_id>', methods=['GET'])
def read_specific_category(cat_id: int) -> Response:
    category = WEPCategory.query.get_or_404(cat_id)
    edit_link = category.make_edit_link() if session.get('user') else ""

    body_html = list()
    body_html.append(f"<h2>Posts in category <em>{category.name}</em> {edit_link}</h2>")
    body_html.append(category.html_serialize_summary())
    body_html.append("<ul>")
    body_html.extend([p.listify() for p in category.associated_posts if p.is_published])
    body_html.append("</ul>")
    inner_html = "\n".join(body_html)
    output = wep_erect(title=category.name, body_html=inner_html)
    return Response(output, mimetype='text/html')


@bp.route('/all', methods=['GET'])
def list_all_categories():
    results = db.session.execute(sql.text("""
        WITH category_occurrences AS (
            SELECT category_id, COUNT(*) AS posts_in_category
            FROM post_categories
            GROUP BY category_id
        ) SELECT c.id, c.name, co.posts_in_category
        FROM category_occurrences co
        INNER JOIN categories c
        ON c.id = co.category_id
        ORDER BY posts_in_category DESC;
    """)).fetchall()

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


@bp.route('/new', methods=['POST'])
def add_new_category():
    cat = WEPCategory(True,
                      datetime.fromisoformat(request.form['creation_date']),
                      datetime.fromisoformat(request.form['last_edit_date']),
                      datetime.fromisoformat(request.form['publication_date']),
                      request.form['name'],
                      request.form['summary'],
                      None)
    try:
        db.session.add(cat)
        db.session.commit()
        return redirect(url_for('home.show_homepage'))
    except SQLAlchemyError as ex:
        abort(400, ex)
