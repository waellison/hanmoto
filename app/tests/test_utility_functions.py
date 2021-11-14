import datetime
import hashlib
import pytest
from .. import utils


def test_encypher_pw():
    cleartext = "hunter2"

    salt, encyphered_password = utils.wep_encypher_pw(cleartext)
    assert encyphered_password == hashlib.sha512((cleartext + salt).encode('utf-8')).hexdigest()


def test_check_some_params_against_set_with_invalid_param():
    allowed_params = {'foo'}
    request = {'spam': 1, 'foo': 2}
    invalid_key = utils.wep_check_some_params_against_set(allowed_params, request)
    assert invalid_key == 'spam'


def test_check_some_params_against_set_with_no_missing_key():
    values = {'a', 'b', 'c'}
    request = {'a': 'foo', 'b': 'bar', 'c': 'baz'}
    missing_key = utils.wep_check_some_params_against_set(values, request)
    assert missing_key == ""


def test_check_all_params_against_set_with_missing_key():
    values = {'a'}
    request = dict()
    missing_key = utils.wep_check_all_params_against_set(values, request)
    assert missing_key == {'a'}


def test_check_all_params_against_set_with_no_missing_key():
    values = {'a'}
    request = {'a': 1}
    missing_key = utils.wep_check_all_params_against_set(values, request)
    assert missing_key == set()


def test_make_gravatar_img_link(author):
    test_hash = hashlib.md5(author.email.strip().lower().encode('utf-8')).hexdigest()
    href = f"https://www.gravatar.com/avatar/{test_hash}.jpg"
    assert utils.wep_make_gravatar_img(author.email) == href


@pytest.mark.parametrize("abbr, month", [("Jan.", 1), ("Feb.", 2), ("March", 3),
                                         ("April", 4), ("May", 5,), ("June", 6),
                                         ("July", 7), ("Aug.", 8), ("Sept.", 9),
                                         ("Oct.", 10), ("Nov.", 11), ("Dec.", 12)])
def test_ap_date_format(abbr: str, month: int):
    date = datetime.datetime(1970, month, 1)
    assert f"{abbr} 1, 1970" == utils.wep_ap_date_format(date)
