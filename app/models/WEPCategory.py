from slugify import slugify
from . import db
from .WEPBaseEntities import WEPEntity, WEPSummarizable, WEPNameable, WEPSluggable

post_categories = db.Table(
    'post_categories',
    db.Column('post_id', db.Integer, db.ForeignKey('posts.id'), primary_key=True),
    db.Column('category_id', db.Integer, db.ForeignKey('categories.id'), primary_key=True)
)


class WEPCategory(WEPEntity, WEPSluggable, WEPSummarizable, WEPNameable):
    __tablename__ = 'categories'

    parent_category = db.Column(db.Integer, db.ForeignKey('categories.id', ondelete="SET NULL"), nullable=True)
    associated_posts = db.relationship('WEPPost',
                                       secondary=post_categories,
                                       lazy='subquery',
                                       backref=db.backref('categories'))

    def __init__(self, is_published, create_date, modify_date, publish_date, name, summary, parent):
        super().__init__(is_published, create_date, modify_date, publish_date)
        self.slug = slugify(name)
        self.name = name
        self.summary = summary
        self.parent_category = parent

    def json_serialize(self) -> dict[str, any]:
        attrs = super().json_serialize()
        attrs['name'] = self.name
        attrs['summary'] = self.summary
        attrs['slug'] = self.slug
        attrs['associated_post_count'] = len(self.associated_posts)
        return attrs

    def linkify(self) -> str:
        return f"<a href='/categories/{self.id}'>{self.name}</a>"

    def listify(self) -> str:
        return f"<li>{self.linkify()} ({len(self.associated_posts)} posts)</li>"
