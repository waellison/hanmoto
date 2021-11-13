from datetime import datetime
from ..models.WEPPost import WEPPost


def test_post_json_serialize(client, author):
    my_post = WEPPost(
                is_published=True,
                create_date=datetime(1970, 1, 1),
                modify_date=datetime(1970, 1, 1),
                publish_date=datetime(1970, 1, 1),
                name="First Post!",
                summary="First post.",
                content="First post.",
                author=author)

    expected_output = {
        "is_published": True,
        "creation_date": "1970-01-01",
        "last_edit_date": "1970-01-01",
        "publication_date": "1970-01-01",
        "name": "First Post!",
        "content": "First post.",
        "slug": "first-post",
        "summary": "First post.",
        "author": {
            "username": "wae",
            "email": "nobody@example.com",
            "avatar": "/images/devnull.jpg"
        }
    }

    assert my_post.json_serialize() == expected_output

