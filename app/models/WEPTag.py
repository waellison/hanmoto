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
from . import db
from .WEPTaxonomic import WEPTaxonomic
from .WEPPost import WEPPost

"""Intermediate table representing the many-to-many
   relationship between posts and categories."""
post_tags = db.Table(
    'post_tags',
    db.Column('post_id', db.Integer, db.ForeignKey('posts.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'), primary_key=True)
)


class WEPTag(WEPTaxonomic):
    """
    Class describing the "Category" entity in WillPress.

    A Tag is a narrow, low-level taxonomy for textual content.  Tags are non-hierarchical.  An
    Uchapishaji user writing about a given video game might tag it as 'Crash Bandicoot'
    (game title), 'Naughty Dog' (developer), 'Universal Interactive Studios' (publisher), and
    '1996' (release year), but it would be categorized under the Sony PlayStation.
    """
    __tablename__ = 'tags'

    """Posts associated with this tag, as an SQLAlchemy backreference.
       This creates the `tags` attribute on `WEPPost` which is a list of
       that post's assigned categories."""
    associated_posts = db.relationship('WEPPost',
                                       secondary=post_tags,
                                       lazy='subquery',
                                       backref=db.backref('tags'))

    def __init__(self, is_published, create_date, modify_date, publish_date, name, summary):
        """
        Create a new category.

        Args:
            is_published: [Boolean] whether the category has been published
            create_date: [datetime] the date the category was created
            modify_date: [datetime] the date the category was last modified
            publish_date: [datetime] the date the category was published
            name: [string] the name of the category
            summary: [string] a summary describing the category
        """
        WEPTaxonomic.__init__(self,
                              "tag",
                              "tags",
                              is_published,
                              create_date,
                              modify_date,
                              publish_date,
                              name,
                              summary)
