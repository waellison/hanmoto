from . import db
from .WEPBaseEntities import WEPEntity, WEPSluggable, WEPSummarizable, WEPNameable


class WEPTaxonomic(WEPEntity, WEPSluggable, WEPSummarizable, WEPNameable):
    """
    Base class for taxonomic entities.  These represent thematic divisions of content.
    """
    __abstract__ = True

    def __init__(self, genre, genre_plural, is_published, create_date, modify_date, publish_date, name, summary):
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
        WEPEntity.__init__(self, is_published, create_date, modify_date, publish_date)
        WEPNameable.__init__(self, name)
        WEPSluggable.__init__(self, self.name)
        WEPSummarizable.__init__(self, summary)
        self.genre = genre
        self.genre_plural = genre_plural

    def __str__(self):
        return WEPNameable.__str__(self)

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

    def _genre(self):
        return self.genre

    def _genre_plural(self):
        return self.genre_plural

    def linkify(self) -> str:
        """
        Creates an HTML anchor linking to the view for this category.

        Returns:
            A string containing an HTML anchor linking to the view for this category.
        """
        return f"<a href='/{self._genre()}/{self.id}'>{self.name}</a>"

    def listify(self) -> str:
        """
        Creates an HTML list entry containing a link to this category and the
        count of its associated posts.

        Returns:
            A string containing an HTML list entry linking to the view for this category.
        """
        return f"<li>{self.linkify()} ({len(self.associated_posts)} posts)</li>"

    def make_edit_link(self) -> str:
        return f"<a href='/admin/{self._genre_plural()}/edit?id={self.id}'>[Edit]</a>"
