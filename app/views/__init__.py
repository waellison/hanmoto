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
from flask import render_template
from flask_admin import Admin

SITE_NAME = "WillPress Test Site"
POSTS_PER_PAGE = 7
admin = Admin()


def wep_erect(template_name="default.html", **kwargs):
    if kwargs.get('site_name', None) is None:
        kwargs['site_name'] = SITE_NAME

    return render_template(template_name, **kwargs)


def wep_make_pagination_links(prev_page: str, next_page: str, sep=" &bull; "):
    if prev_page or next_page:
        print("<p class='pagination-nav'>")

    if prev_page:
        print(prev_page)

    if prev_page and next_page:
        print(sep)

    if next_page:
        print(next_page)

    if prev_page or next_page:
        print("</p>")
