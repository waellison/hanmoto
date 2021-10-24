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
from slugify import slugify
from ..utils import wep_ap_date_format
from .WEPBaseEntities import WEPEntity, WEPSummarizable, WEPNameable, WEPSluggable, WEPContentful


class WEPPost(WEPEntity, WEPSluggable, WEPSummarizable, WEPNameable, WEPContentful):
    """
    Model class for posts.

    A post is a date-stamped content entity attributed to an author.  It consists of
    the content, an optional summary of that content, a name, a slug derived from the
    name, and the standard attributes of all WEPEntity instances.
    """
    __tablename__ = "posts"

    def __init__(self, is_published, create_date, modify_date, publish_date, name, summary, content):
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
        """
        super().__init__(is_published, create_date, modify_date, publish_date)
        self.slug = slugify(name)
        self.name = name
        self.content = content
        self.summary = summary

    def json_serialize(self) -> dict[str, any]:
        """
        Serialize a post into a format fit for JSON.

        Returns:
            A dict containing the post's attributes
        """
        attrs = super().json_serialize()
        attrs['name'] = self.name
        attrs['summary'] = self.summary
        attrs['slug'] = self.slug
        attrs['content'] = self.content
        return attrs

    def listify(self):
        """
        Create an HTML list item from a post.

        Returns:
            A string containing a link to the post, formatted as an HTML list item.
        """
        return f"<li><a href='/posts/{self.id}'>{self.name}</a> (posted {wep_ap_date_format(self.publication_date)})</li>"
