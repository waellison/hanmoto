from slugify import slugify
from . import db
from .WEPBaseEntities import WEPEntity, WEPSummarizable, WEPNameable, WEPSluggable, WEPContentful

post_categories = db.Table(
    'post_categories',
    db.Column('post_id', db.Integer, db.ForeignKey('posts.id'), primary_key=True),
    db.Column('category_id', db.Integer, db.ForeignKey('categories.id'), primary_key=True)
)


class WEPCategory(WEPEntity, WEPSluggable, WEPSummarizable, WEPNameable, WEPContentful):
    __tablename__ = 'categories'

    parent_category = db.Column(db.Integer, db.ForeignKey('categories.id', ondelete="SET NULL"), nullable=True)
    associated_posts = db.relationship('WEPPost',
                                       secondary=post_categories,
                                       lazy='subquery',
                                       backref=db.backref('categories'))

    def __init__(self, published_p, created, last_edited, published_date, name, summary, parent, content):
        super(WEPEntity).__init__(published_p, created, last_edited, published_date)
        super(WEPSummarizable).__init__(summary)
        super(WEPSluggable).__init__(name)
        super(WEPNameable).__init__(name)
        super(WEPContentful).__init__(content)
        self.parent_category = parent

    def json_serialize(self) -> dict[str, any]:
        attrs = super().json_serialize()
        attrs['name'] = self.name
        attrs['summary'] = self.summary
        attrs['slug'] = self.slug
        attrs['content'] = self.content
        attrs['associated_post_count'] = len(self.associated_posts)
        return attrs
