"""Category model for WillPress.

A category is a high-level descriptive categorization for posts.
Categories are hierarchical and are intended to describe broad
categorizations of posts.

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


post_categories = db.Table(
    'post_categories',
    db.Column('post_id', db.Integer, db.ForeignKey('posts.id'), primary_key=True),
    db.Column('category_id', db.Integer, db.ForeignKey('categories.id'), primary_key=True)
)


class WEPCategory:
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    slug = db.Column(db.String(90), nullable=False)
    name = db.Column(db.String(90), nullable=False)
    summary = db.Column(db.String, nullable=False)
    parent_category = db.Column(db.Integer,
                                db.ForeignKey('categories.id', ondelete="SET NULL"),
                                nullable=True)
    associated_posts = db.relationship('WEPPost',
                                       secondary=post_categories,
                                       lazy='subquery',
                                       backref=db.backref('categories'))

    def __init__(self, name: str, summary: str, parent: int = None):
        self.name = name
        self.summary = summary
        self.parent_category = parent
        self.slug = slugify(name)

    def html_serialize(self) -> str:
        markdown = Markdown()
        return smartypants(markdown.convert(source=self.summary))

    def json_serialize(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "slug": self.slug,
            "taxonomyType": "category",
            "summary": self.summary,
            "parentCategoryId": self.parent_category,
            "associatedPosts": len(self.associated_posts)
        }
