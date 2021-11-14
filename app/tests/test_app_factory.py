from .. import wep_create_app


def test_app_factory():
    app = wep_create_app(True)
    assert app is not None
