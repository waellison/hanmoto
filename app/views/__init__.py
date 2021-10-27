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


SITE_NAME = "WillPress Test Site"
POSTS_PER_PAGE = 7


def wep_erect(**kwargs):
    tmpl = Template(filename='./templates/default.mako')
    return tmpl.render(site_name=SITE_NAME, user=session.get('user', None), **kwargs)
