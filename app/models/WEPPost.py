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
from markdown import Markdown
from smartypants import smartypants
from slugify import slugify
from .. import wep_ap_date_format
from .WEPBaseEntities import WEPEntity, WEPSummarizable, WEPNameable, WEPSluggable, WEPContentful


class WEPPost(WEPEntity, WEPSluggable, WEPSummarizable, WEPNameable, WEPContentful):
    __tablename__ = "posts"

    def __init__(self, is_published, create_date, modify_date, publish_date, name, summary, content):
        super().__init__(is_published, create_date, modify_date, publish_date)
        self.slug = slugify(name)
        self.name = name
        self.content = content
        self.summary = summary

    def json_serialize(self) -> dict[str, any]:
        attrs = super().json_serialize()
        attrs['name'] = self.name
        attrs['summary'] = self.summary
        attrs['slug'] = self.slug
        attrs['content'] = self.content
        return attrs

    def listify(self):
        return f"<li><a href='/posts/{self.id}'>{self.name}</a> (posted {wep_ap_date_format(self.publication_date)})</li>"
