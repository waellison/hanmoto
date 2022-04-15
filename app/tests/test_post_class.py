def test_post_stringize(test_post):
    assert str(test_post) == "First Post!"


def test_post_json_serialize(test_post, author):
    expected_output = {
        "is_published": True,
        "categories": [],
        "tags": [],
        "id": None,    # only populates w/ a database connection
        "name": "First Post!",
        "content": "First post.",
        "slug": "first-post",
        "summary": "First post.",
    }

    assert test_post.json_serialize() == expected_output
