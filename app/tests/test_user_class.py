from ..models import WEPUser


def test_stringize_user(author):
    assert str(author) == "wae"


def test_user_json_serialize(author):
    expected = {
        "username": "wae",
        "email": "nobody@example.com",
        "avatar": "/images/devnull.jpg",
        "posts": []
    }
    assert author.json_serialize() == expected
