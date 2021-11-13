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
from flask import session
from slugify import slugify
from . import db
from ..utils import wep_ap_date_format
from .WEPBaseEntities import WEPEntity, WEPSummarizable, WEPNameable, WEPSluggable, WEPContentful
from .WEPUser import WEPUser


class WEPPost(WEPEntity, WEPSluggable, WEPSummarizable, WEPNameable, WEPContentful):
    """
    Model class for posts.

    A post is a date-stamped content entity attributed to an author.  It consists of
    the content, an optional summary of that content, a name, a slug derived from the
    name, and the standard attributes of all WEPEntity instances.
    """
    __tablename__ = "posts"

    author = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    post_author = db.relationship('WEPUser', backref=db.backref('posts'))

    def __init__(self, is_published, create_date, modify_date, publish_date, name, summary, content, author):
        """
        Create a new post.

        Args:
            is_published: [boolean] whether the post is published or not
            create_date: [datetime] the date the post was created
            modify_date: [datetime] the date the post was last modified
            publish_date: [datetime] the date the post was published
            name: [string] the name of the post
            summary: [string] a Markdown-formatted string containing a brief summary of the post
            content: [string] a Markdown-formatted string containing the post's content
            author: [integer] key to the author of this post
        """
        WEPEntity.__init__(self, is_published, create_date, modify_date, publish_date)
        WEPSummarizable.__init__(self, summary)
        WEPContentful.__init__(self, content)
        WEPNameable.__init__(self, name)
        WEPSluggable.__init__(self, name)
        self.author = author

    def __str__(self):
        return self.name

    def json_serialize(self) -> dict[str, any]:
        """
        Serialize a post into a format fit for JSON.

        Returns:
            A dict containing the post's attributes
        """
        attrs = WEPEntity.json_serialize(self)
        attrs['name'] = WEPNameable.json_serialize(self)["name"]
        attrs['summary'] = WEPSummarizable.json_serialize(self)
        attrs['slug'] = WEPSluggable.json_serialize(self)["slug"]
        attrs['content'] = WEPContentful.json_serialize(self)
        attrs['author'] = self.author.json_serialize()
        return attrs

    def linkify(self, presigil="", postsigil=""):
        return f"<a href='/posts/{self.id}'>{presigil}{self.name}{postsigil}</a>"

    def listify(self):
        """
        Create an HTML list item from a post.

        Returns:
            A string containing a link to the post, formatted as an HTML list item.
        """
        return f"<li>{self.linkify()} (posted {wep_ap_date_format(self.publication_date)})</li>"

    def html_serialize_author(self):
        edit_link = f"<a href='/admin/posts/edit?id={self.id}'>[Edit]</a>" if session.get('user', None) else ""
        return f"<p>Written by {self.post_author.html_serialize()} on {wep_ap_date_format(self.publication_date)} {edit_link}</p>"
