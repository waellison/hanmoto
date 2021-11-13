"""Base entities for the models in WillPress.

"An Excellent Blog Engine"

Copyright (c) 2021 by William Ellison.  This program is licensed under
the terms of the Do What the Fuck You Want To Public License, version 2
or later, as described in the COPYING file at the root of this
distribution.

William Ellison
<waellison@gmail.com>
October 2021
"""
import datetime
from markdown import Markdown
from smartypants import smartypants
from slugify import slugify
from . import db


class WEPEntity(db.Model):
    """
    Base entity for all WillPress model classes that represent publishable content.
    """
    __abstract__ = True

    """The serial ID of the entity."""
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    """Whether the entity is actively published."""
    is_published = db.Column(db.Boolean, nullable=False, default=False)

    """When the entity was created."""
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())

    """When the entity was last modified."""
    last_edit_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())

    """When the entity was published.  Is set to None if the entity is not yet published."""
    publication_date = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, is_published: bool, creation_date: datetime, last_edit_date: datetime, publication_date: datetime):
        """
        Create a new base entity.

        Args:
            is_published: [Boolean] True if the item is published, False otherwise
            creation_date: [datetime] the date of creation of the entity
            last_edit_date: [datetime] the date of last modification of the entity
            publication_date: [datetime] the date on which the entity was published, None if not yet published
        """
        self.is_published = is_published
        self.creation_date = creation_date
        self.last_edit_date = last_edit_date
        self.publication_date = publication_date

    def json_serialize(self) -> dict[str, any]:
        """
        Converts the entity into a form suitable to be serialized into JSON.

        Returns:
            A dict containing the entity's attributes.
        """
        return {
            'is_published': self.is_published,
            'creation_date': self.creation_date.isoformat(),
            'publication_date': self.publication_date.isoformat(),
            'modification_date': self.last_edit_date.isoformat()
        }


class WEPSummarizable(db.Model):
    """
    Represents an entity which has the attribute of having a summary bound to it.

    A summary is a brief text blurb describing the entity in a brief fashion.
    """
    __abstract__ = True

    """The summary pertaining to this entity.  Stored as Markdown text."""
    summary = db.Column(db.String(270), nullable=True)

    def __init__(self, summary):
        self.summary = summary

    def html_serialize(self) -> str:
        """
        Converts an entity's summary into HTML output.

        Returns:
            The entity's summary converted to HTML, as a string.
        """
        markdown = Markdown()
        return smartypants(markdown.convert(source=self.summary))

    def json_serialize(self) -> dict:
        return {"body": self.html_serialize(),
                "mime_type": "text/html"}


class WEPNameable(db.Model):
    """
    Represents an entity which has the attribute of having a name associated with it.

    A name is a short string by which this entity is known.
    """
    __abstract__ = True
    name = db.Column(db.String(90), nullable=False)

    def __init__(self, name):
        self.name = name

    def json_serialize(self) -> dict:
        return {"name": self.name}


class WEPSluggable(db.Model):
    """
    Represents an entity which has the attribute of having a slug associated with it.

    A slug is a lowercase, hyphen-separated string suitable for URLs.
    """
    __abstract__ = True

    """A lowercase, hyphen-separated string suitable for URLs."""
    slug = db.Column(db.String(90), nullable=False)

    def __init__(self, name):
        self.slug = slugify(name)

    def json_serialize(self):
        return {"slug": self.slug}


class WEPContentful(db.Model):
    """
    Represents an entity which has the attribute of containing content.

    Content is simply longform text associated with an entity.
    """
    __abstract__ = True

    """Longform text associated with an entity, stored as Markdown source."""
    content = db.Column(db.Text)

    def __init__(self, content):
        self.content = content

    def json_serialize(self) -> dict:
        return {"body": self.html_serialize(),
                "mime_type": "text/html"}

    def html_serialize(self) -> str:
        """
        Converts an entity's text into HTML.

        Returns:
            The entity's text as HTML.
        """
        markdown = Markdown()
        return smartypants(markdown.convert(source=self.content))
