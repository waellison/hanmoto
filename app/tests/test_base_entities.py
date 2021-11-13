from datetime import datetime
from ..models.WEPBaseEntities import (
    WEPEntity,
    WEPSluggable,
    WEPSummarizable,
    WEPNameable,
    WEPContentful
)


def test_wep_entity_to_json():
    entity = WEPEntity(True,
                       datetime(1970, 1, 1),
                       datetime(1970, 1, 1),
                       datetime(1970, 1, 1))
    expected = {
        "is_published": True,
        "creation_date": "1970-01-01T00:00:00",
        "publication_date": "1970-01-01T00:00:00",
        "modification_date": "1970-01-01T00:00:00",
    }
    assert expected == entity.json_serialize()


def test_summarizable_entity_to_json():
    entity = WEPSummarizable("This is the summary.")
    expected = {"body": "<p>This is the summary.</p>",
                "mime_type": "text/html"}
    assert expected == entity.json_serialize()


def test_nameable_entity_to_json():
    entity = WEPNameable("My Name Is Slim Shady")
    expected = {"name": "My Name Is Slim Shady"}
    assert expected == entity.json_serialize()


def test_sluggable_entity_to_json():
    entity = WEPSluggable("My Name is Slim Shady")
    expected = {"slug": "my-name-is-slim-shady"}
    assert expected == entity.json_serialize()


def test_contentful_entity_to_json():
    entity = WEPContentful("This is some content.")
    expected = {"body": "<p>This is some content.</p>",
                "mime_type": "text/html"}
    assert expected == entity.json_serialize()
