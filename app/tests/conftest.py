from datetime import datetime
import pytest
from .. import wep_create_app
from ..models.WEPUser import WEPUser
from ..models.WEPPost import WEPPost


@pytest.fixture
def client():
    app = wep_create_app()
    with app.test_client() as client:
        yield client


@pytest.fixture
def author():
    user = WEPUser(
        username="wae",
        password="hunter2",
        salt="itdoesnthavetomakesense",
        email="nobody@example.com",
        avatar="/images/devnull.jpg"
    )

    return user


@pytest.fixture
def test_post(author):
    return WEPPost(is_published=True,
                   name="First Post!",
                   summary="First post.",
                   content="First post.",
                   author=author)
