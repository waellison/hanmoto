"""
User and author classes for WillPress.

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

    username = db.Column(db.String(16), nullable=False, unique=True
                      index=db.Index('username_idx',
                      postgresql_using='hash'))

    def __init__(self, user_id, username):
        self.user_id = user_id

