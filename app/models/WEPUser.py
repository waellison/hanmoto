"""User and author classes for WillPress.

"An Excellent Blog Engine"

A User is an entity representing a user of WillPress.

Copyright (c) 2021 by William Ellison.  This program is licensed under
the terms of the Do What the Fuck You Want To Public License, version 2
or later, as described in the COPYING file at the root of this
distribution.

William Ellison

<waellison@gmail.com>
October 2021
"""
from . import db


class WEPUser(db.Model):
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(16), nullable=False, unique=True,
                         index=db.Index('username_idx', postgresql_using='hash'))
    password = db.Column(db.String(128), nullable=False)
    salt = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(64), nullable=False, unique=True)
    avatar = db.Column(db.String, nullable=False)

    def __init__(self, username: str, password: str, salt: str, email: str, avatar: str):
        self.username = username
        self.password = password
        self.salt = salt
        self.email = email
        self.avatar = avatar

    def __str__(self):
        return self.username

    def json_serialize(self):
        return {
            'username': self.username,
            'email': self.email,
            'avatar': self.avatar
        }

    def html_serialize(self):
        return f"<a href='/users/{self.user_id}>{self.username}</a>"
