Welcome to Uchapishaji
--------------------

.. image:: https://api.codacy.com/project/badge/Grade/bdbb12c7597e40c9b3e0fa8b7c39a5bb
   :alt: Codacy Quality Badge
   :target: https://app.codacy.com/gh/tnwae/uchapishaji?utm_source=github.com&utm_medium=referral&utm_content=tnwae/uchapishaji&utm_campaign=Badge_Grade_Settings

.. image:: https://api.codacy.com/project/badge/Coverage/bdbb12c7597e40c9b3e0fa8b7c39a5bb
   :alt: Codacy Coverage Badge
   :target: https://app.codacy.com/gh/tnwae/uchapishaji?utm_source=github.com&utm_medium=referral&utm_content=tnwae/uchapishaji&utm_campaign=Badge_Coverage_Settings

.. image:: https://github.com/tnwae/uchapishaji/actions/workflows/python-app.yml/badge.svg
   :alt: Python-App
   :target: https://github.com/tnwae/uchapishaji/actions/workflows/python-app.yml

*Uchapishaji* is a modern blog engine for the ancient Web.  It is designed
to present content in a way suitable for any template but also to expose
a REST API that can be consumed by clients for legacy devices on any
operating system capable of using TCP/IP and with any language capable
of sending HTTP requests over the network and consuming JSON-formatted
responses.

Uchapishaji is based on the Flask framework and uses SQLAlchemy to
communicate with the backing store.  I have designed Uchapishaji to work
with PostgreSQL as it is the database (and, consequently, the SQL
dialect) that I know the best, but nothing in the design of Uchapishaji
should preclude using it with other databases like MySQL/MariaDB,
MS-SQL, Oracle, or SQLite.

Uchapishaji is going to use Markdown as its input language for markup and
Mako for templates.  The choice of a frontend library is up to you; I am
going to use my own templates, a few JavaScript files here and there,
and my Sass library called *The Chain*.

Attributions
============
The database schema used by Uchapishaji is based on a schema devised by
`The Code Blogger`_ originally for use with the .NET libraries.  I have
adapted this schema for use with Python and SQLAlchemy.

`Markdown`_ was originally created by John Gruber.

*Uchapishaji* is the Swahili word for "printing press."

.. _The Code Blogger: https://thecodeblogger.com/2021/06/25/database-schema-for-blog-management-using-net-ef-core/
.. _Markdown: https://daringfireball.net/projects/markdown
