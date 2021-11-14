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
from slugify import slugify
from . import db
from .WEPBaseEntities import WEPEntity, WEPSummarizable, WEPNameable, WEPSluggable
from .WEPPost import WEPPost

"""Intermediate table representing the many-to-many
   relationship between posts and categories."""
post_categories = db.Table(
    'post_categories',
    db.Column('post_id', db.Integer, db.ForeignKey('posts.id'), primary_key=True),
    db.Column('category_id', db.Integer, db.ForeignKey('categories.id'), primary_key=True)
)


class WEPCategory(WEPEntity, WEPSluggable, WEPSummarizable, WEPNameable):
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
        super().__init__(is_published, create_date, modify_date, publish_date)
        self.slug = slugify(name)
        self.name = name
        self.summary = summary
        self.parent_category = parent

    def __str__(self):
        return self.name

    def json_serialize(self) -> dict[str, any]:
        """
        Converts a category object to be serialized into JSON.

        Return s:
            A dict containing all the attributes of this category object.
        """
        attrs = super().json_serialize()
        attrs['id'] = self.id
        attrs['name'] = self.name
        attrs['summary'] = self.summary
        attrs['slug'] = self.slug
        attrs['associated_post_count'] = len(self.associated_posts)
        return attrs

    def html_serialize(self) -> dict[str, any]:
        attrs = dict()
        attrs['id'] = self.id
        attrs['name'] = WEPNameable.html_serialize(self)
        attrs['summary'] = WEPSummarizable.html_serialize(self)
        attrs['slug'] = WEPSluggable.json_serialize(self)["slug"]
        attrs['associated_post_count'] = len(self.associated_posts)
        return attrs

    def linkify(self) -> str:
        """
        Creates an HTML anchor linking to the view for this category.

        Returns:
            A string containing an HTML anchor linking to the view for this category.
        """
        return f"<a href='/categories/{self.id}'>{self.name}</a>"

    def listify(self) -> str:
        """
        Creates an HTML list entry containing a link to this category and the
        count of its associated posts.

        Returns:
            A string containing an HTML list entry linking to the view for this category.
        """
        return f"<li>{self.linkify()} ({len(self.associated_posts)} posts)</li>"

    def make_edit_link(self) -> str:
        return f"<a href='/admin/categories/edit?id={self.id}'>[Edit]</a>"
