"""Views for WillPress.

"An Excellent Blog Engine"

Copyright (c) 2021 by William Ellison.  This program is licensed under
the terms of the Do What the Fuck You Want To Public License, version 2
or later, as described in the COPYING file at the root of this
distribution.

William Ellison
<waellison@gmail.com>
October 2021
"""
from mako.template import Template
from flask import session
from flask_admin import Admin

SITE_NAME = "WillPress Test Site"
POSTS_PER_PAGE = 7
admin = Admin()


def wep_erect(**kwargs):
    tmpl = Template(filename='./templates/default.mako')
    return tmpl.render(site_name=SITE_NAME, user=session.get('user', None), **kwargs)


def wep_make_pagination_links(prev_page: str, next_page: str, body_html: list, sep=" &bull; "):
    if prev_page or next_page:
        body_html.append("<p class='pagination-nav'>")

    if prev_page:
        body_html.append(prev_page)

    if prev_page and next_page:
        body_html.append(sep)

    if next_page:
        body_html.append(next_page)

    if prev_page or next_page:
        body_html.append("</p>")
