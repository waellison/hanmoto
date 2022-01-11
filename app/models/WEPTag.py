"""Tag model for Uchapishaji.

A tag is a low-level descriptive categorization for posts.
Tags are non-hierarchical and are meant to describe individual
posts that share a common theme.

"An Excellent Blog Engine"

Copyright (c) 2021 by William Ellison.  This program is licensed under
the terms of the Do What the Fuck You Want To Public License, version 2
or later, as described in the COPYING file at the root of this
distribution.

William Ellison
<waellison@gmail.com>
October 2021
"""
from markdown import Markdown
from smartypants import smartypants
from slugify import slugify
from . import db
from .WEPPost import WEPPost


post_tags = db.Table(
    'post_tags',
    db.Column('post_id', db.Integer, db.ForeignKey('posts.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'), primary_key=True)
)


class WEPTag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    slug = db.Column(db.String(90), nullable=False)
    name = db.Column(db.String(90), nullable=False)
    summary = db.Column(db.Text, nullable=False)

    associated_posts = db.relationship('WEPPost',
                                       secondary=post_tags,
                                       lazy='subquery',
                                       backref=db.backref('tags'))

    def __init__(self, name: str, summary: str):
        self.name = name
        self.summary = summary
        self.slug = slugify(name)

    def html_serialize(self) -> str:
        markdown = Markdown()
        return smartypants(markdown.convert(source=self.summary))

    def json_serialize(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "slug": self.slug,
            "taxonomyType": "tag",
            "summary": self.summary,
            "associatedPosts": [p.json_serialize() for p in self.associated_posts]
        }
