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
from . import db
from .WEPBaseEntities import WEPEntity, WEPSummarizable, WEPNameable, WEPSluggable, WEPContentful, WEPHtmlSerializable


class WEPPost(WEPEntity, WEPSluggable, WEPSummarizable, WEPNameable, WEPContentful, WEPHtmlSerializable):
    __tablename__ = "posts"

    def __init__(self, is_published, creation_date, last_edit_date, publication_date, name, summary, content):
        super(WEPEntity).__init__(is_published, creation_date, last_edit_date, publication_date)
        super(WEPSluggable).__init__(name)
        super(WEPNameable).__init__(name)
        super(WEPSummarizable).__init__(summary)
        super(WEPContentful).__init__(content)

    def json_serialize(self) -> dict[str, any]:
        attrs = super().json_serialize()
        attrs['name'] = self.name
        attrs['summary'] = self.summary
        attrs['slug'] = self.slug
        attrs['contents'] = self.content
        return attrs
