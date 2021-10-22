"""
Post class for WillPress.

"An Excellent Blog Engine"

A Post is a date-stamped article assigned to an author.  It consists of
its text, its author, its datestamp, and other attributes as required.

Copyright (c) 2021 by William Ellison.  This program is licensed under
the terms of the Do What the Fuck You Want To Public License, version 2
or later, as described in the COPYING file at the root of this
distribution.

William Ellison
<waellison@gmail.com>
October 2021
"""
from . import db


class WEPPost(db.Model):
    __tablename__ = "posts"

    post_id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    title = db.Column(db.String(256), nullable=False,
                      index=db.Index('post_title_idx',
                      postgresql_using='hash'))

#    author_id = db.Column(db.Integer, db.ForeignKey(authors.id),
#                          nullable=False)

    text = db.Column(db.Text)

    def __init__(self, post_id, title, author_id, text):
        self.post_id = post_id
        self.title = title
        self.author_id = author_id
        self.text = text
