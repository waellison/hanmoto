Welcome to Willpress
--------------------

.. image:: https://api.codacy.com/project/badge/Grade/434cd26cf50743edbd8ef941b473ff4e
   :alt: Codacy Badge
   :target: https://app.codacy.com/gh/waellison/willpress?utm_source=github.com&utm_medium=referral&utm_content=waellison/willpress&utm_campaign=Badge_Grade_Settings

*Willpress* is a modern blog engine for the ancient Web.  It is designed
to present content in a way suitable for any template but also to expose
a REST API that can be consumed by clients for legacy devices on any
operating system capable of using TCP/IP and with any language capable
of sending HTTP requests over the network and consuming JSON-formatted
responses.

Willpress is based on the Flask framework and uses SQLAlchemy to
communicate with the backing store.  I have designed Willpress to work
with PostgreSQL as it is the database (and, consequently, the SQL
dialect) that I know the best, but nothing in the design of Willpress
should preclude using it with other databases like MySQL/MariaDB,
MS-SQL, Oracle, or SQLite.

Attributions
============
The database schema used by Willpress is based on a schema devised by
`The Code Blogger`_ originally for use with the .NET libraries.  I have
adapted this schema for use with Python and SQLAlchemy.

`Markdown`_ was originally created by John Gruber.

.. _The Code Blogger: https://thecodeblogger.com/2021/06/25/database-schema-for-blog-management-using-net-ef-core/
.. _Markdown: https://daringfireball.net/projects/markdown

