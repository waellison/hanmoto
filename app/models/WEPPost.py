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
from datetime import datetime
from slugify import slugify
from markdown import Markdown
from smartypants import smartypants
from . import db
from ..utils import wep_ap_date_format
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
    author = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    post_author = db.relationship('WEPUser', backref=db.backref('posts'))

    def __init__(self, name: str, summary: str, content: str, author: int, is_published: bool = False):
        self.name = name
        self.summary = summary
        self.content = content
        self.slug = slugify(name)
        self.is_published = is_published
        self.author = author

    def __str__(self):
        return self.name

    def json_serialize(self) -> dict[str, any]:
        return {
            "id": self.id,
            "name": self.name,
            "slug": self.slug,
            "tags": [t.json_serialize() for t in self.tags],
            "categories": [c.json_serialize() for c in self.categories],
            "summary": self.summary,
            "content": self.content,
        }

    def html_serialize(self, title_level=2) -> dict[str, str]:
        attrs = dict()
        markdown = Markdown()
        attrs['name'] = f"<h{title_level}>{self.name}</h{title_level}>"
        attrs['summary'] = smartypants(markdown.convert(source=self.summary))
        attrs['content'] = smartypants(markdown.convert(source=self.content))
        attrs['post_date'] = wep_ap_date_format(self.publication_date)
        attrs['tags'] = [t.json_serialize() for t in self.tags]
        attrs['categories'] = [c.json_serialize() for c in self.categories]
        return attrs
