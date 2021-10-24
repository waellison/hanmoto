import datetime
from slugify import slugify
from markdown import Markdown
from smartypants import smartypants
from . import db


class WEPEntity(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    is_published = db.Column(db.Boolean, nullable=False, default=False)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())
    last_edit_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())
    publication_date = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, is_published: bool, creation_date: datetime, last_edit_date: datetime, publication_date: datetime):
        self.is_published = is_published
        self.creation_date = creation_date
        self.last_edit_date = last_edit_date
        self.publication_date = publication_date

    def json_serialize(self) -> dict[str, any]:
        return {
            'id': self.id,
            'is_published': self.is_published,
            'creation_date': self.creation_date.isoformat(),
            'publication_date': self.publication_date.isoformat(),
            'last_edit_date': self.last_edit_date.isoformat()
        }


class WEPSummarizable(db.Model):
    __abstract__ = True
    summary = db.Column(db.String(270), nullable=True)

    def html_serialize_summary(self):
        markdown = Markdown()
        return smartypants(markdown.convert(source=self.summary))


class WEPNameable(db.Model):
    __abstract__ = True
    name = db.Column(db.String(90), nullable=False)

    def html_serialize_name(self, level=1):
        return f"<h{level}>{self.name}</h{level}>"


class WEPSluggable(db.Model):
    __abstract__ = True
    slug = db.Column(db.String(90), nullable=False)


class WEPContentful(db.Model):
    __abstract__ = True
    content = db.Column(db.Text)

    def html_serialize_content(self):
        markdown = Markdown()
        return smartypants(markdown.convert(source=self.content))
