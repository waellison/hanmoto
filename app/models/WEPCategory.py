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
from . import db
from .WEPTaxonomic import WEPTaxonomic
from .WEPPost import WEPPost

"""Intermediate table representing the many-to-many
   relationship between posts and categories."""
post_categories = db.Table(
    'post_categories',
    db.Column('post_id', db.Integer, db.ForeignKey('posts.id'), primary_key=True),
    db.Column('category_id', db.Integer, db.ForeignKey('categories.id'), primary_key=True)
)


class WEPCategory(WEPTaxonomic):
    """
    Class describing the "Category" entity in WillPress.

    A Category is a broad, high-level taxonomy for textual content.  Categories may be sorted into
    hierarchical groupings.  For example, a WillPress user writing about video games might have one
    category for seventh-generation console games, with subcategories for PlayStation 3 and Xbox
    360.
    """
    __tablename__ = 'categories'

    """Category's parent, as an id within the categories table."""
    parent_category = db.Column(db.Integer, db.ForeignKey('categories.id', ondelete="SET NULL"), nullable=True)

    """Posts associated with this category, as an SQLAlchemy backreference.
       This creates the `categories` attribute on `WEPPost` which is a list of
       that post's assigned categories."""
    associated_posts = db.relationship('WEPPost',
                                       secondary=post_categories,
                                       lazy='subquery',
                                       backref=db.backref('categories'))

    def __init__(self, is_published, create_date, modify_date, publish_date, name, summary, parent):
        """
        Create a new category.

        Args:
            is_published: [Boolean] whether the category has been published
            create_date: [datetime] the date the category was created
            modify_date: [datetime] the date the category was last modified
            publish_date: [datetime] the date the category was published
            name: [string] the name of the category
            summary: [string] a summary describing the category
            parent: [int] the numeric id of another category which is the parent of this one
        """
        WEPTaxonomic.__init__(self,
                              "category",
                              "categories",
                              is_published,
                              create_date,
                              modify_date,
                              publish_date,
                              name,
                              summary)
        self.parent_category = parent
