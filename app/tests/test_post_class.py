def test_post_stringize(test_post):
    assert str(test_post) == "First Post!"


def test_post_json_serialize(test_post, author):
    expected_output = {
        "is_published": True,
        "creation_date": "1970-01-01T00:00:00",
        "modification_date": "1970-01-01T00:00:00",
        "publication_date": "1970-01-01T00:00:00",
        "name": "First Post!",
        "content": {
            "body": "<p>First post.</p>",
            "mime_type": "text/html"
        },
        "slug": "first-post",
        "summary": {
            "body": "<p>First post.</p>",
            "mime_type": "text/html"
        },
        "author": {
            "username": "wae",
            "email": "nobody@example.com",
            "avatar": "/images/devnull.jpg"
        }
    }

    assert test_post.json_serialize() == expected_output
