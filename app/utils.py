import secrets
import hashlib
import sys
from datetime import datetime


def wep_encypher_pw(password: str, salt=None) -> (str, str):
    """
    Hash and salt a password string and return the SHA-512 digest of the
    hashed and salted string.
    Args:
        password: A password inputted by the user
        salt: The salt to apply to the password before hashing

    Returns:
        The SHA-512 message digest, in hexadecimal form, of the password
        string with a salt applied, along with the salt itself.
    """
    if not salt:
        salt = secrets.token_hex(16)
    return salt, hashlib.sha512((password + salt).encode('utf-8')).hexdigest()


def wep_check_some_params_against_set(valid_params: set, request: dict) -> str:
    """
    Check one or more request parameters against a set of valid inputs.

    Args:
        valid_params: a set of valid parameters
        request: the request object containing zero or more parameters

    Returns:
        The invalid key if one is determined to be invalid
    """
    for key in request.keys():
        if key not in valid_params:
            return key
    return ""


def wep_make_gravatar_img(email: str) -> str:
    """
    Returns a string pointing to a Gravatar image based on an email address.

    Args:
        email: the email associated with a given Gravatar image

    Returns:
        a link of the form <https://www.gravatar.com/avatar/:hash>, where
        `hash` is the MD5 hash of the email with whitespace trimmed and
        in all lowercase.
    """
    email_hash = hashlib.md5(email.strip().lower().encode('utf-8')).hexdigest()
    return f"https://www.gravatar.com/avatar/{email_hash}.jpg"


def wep_check_all_params_against_set(valid_params: set, request: dict) -> set:
    """
    Check an entire request against a set of valid parameters.

    :param valid_params: a set of valid parameters
    :param request: the request object containing zero or more parameters
    :return: The missing parameters, as a set, if the request is invalid.
    """
    set_diff = valid_params.difference(set(request.keys()))
    return set_diff


def wep_ap_date_format(date: datetime) -> str:
    abbreviations = {
        "months": [
            "Jan.",
            "Feb.",
            "March",
            "April",
            "May",
            "June",
            "July",
            "Aug.",
            "Sept.",
            "Oct.",
            "Nov.",
            "Dec."
        ]
    }
    day = date.day
    month = abbreviations["months"][date.month - 1]
    year = date.year
    return f"{month} {day}, {year}"
