"""Post class for WillPress.

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
import typing
from datetime import datetime
from slugify import slugify
from . import db
from .WEPUser import WEPUser


class WEPPost(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    is_published = db.Column(db.Boolean, nullable=False, default=False)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.now())
    last_edit_date = db.Column(db.DateTime, nullable=False, default=datetime.now())
    publication_date = db.Column(db.DateTime, default=datetime.now())
    name = db.Column(db.String(90), nullable=False)
    slug = db.Column(db.String(90), nullable=False)
    content = db.Column(db.Text, nullable=False)
    summary = db.Column(db.Text, nullable=False)
    author = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    post_author = db.relationship("WEPUser", backref=db.backref("posts"))

    def __init__(
        self,
        name: str,
        summary: str,
        content: str,
        author: int,
        is_published: bool = False,
    ):
        self.name = name
        self.summary = summary
        self.content = content
        self.slug = slugify(name)
        self.is_published = is_published
        self.author = author

    def __str__(self):
        return self.name

    def json_serialize(self) -> dict[str, typing.Any]:
        """
        Converts a post object into a dict that can be represented by JSON.
        """
        return {
            "id": self.id,
            "name": self.name,
            "slug": self.slug,
            "categories": [c.json_serialize() for c in self.categories],
            "tags": [t.json_serialize() for t in self.tags],
            "summary": self.summary,
            "content": self.content,
            "is_published": self.is_published,
        }
