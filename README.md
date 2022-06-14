# Hanmoto

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/dfbc8f722a5e4eef81e8f35c8ee1f206)](https://www.codacy.com/gh/waellison/hanmoto/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=waellison/hanmoto&amp;utm_campaign=Badge_Grade)
[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/dfbc8f722a5e4eef81e8f35c8ee1f206)](https://www.codacy.com/gh/waellison/hanmoto/dashboard?utm_source=github.com&utm_medium=referral&utm_content=waellison/hanmoto&utm_campaign=Badge_Coverage)
[![build](https://github.com/waellison/hanmoto/actions/workflows/pytest.yml/badge.svg)](https://github.com/waellison/hanmoto/actions/workflows/pytest.yml)
[![CodeQL](https://github.com/waellison/hanmoto/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/waellison/hanmoto/actions/workflows/codeql-analysis.yml)
[![License](https://img.shields.io/github/license/waellison/hanmoto)](#)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

_Hanmoto_ is a blog engine.  It is designed to expose a REST API that
can be consumed by a mobile client, SPA frontend, or any other client
software that can communicate in JSON.  The _Insatsu_ project
(<https://github.com/waellison/insatsu>) is a representative example.

Hanmoto is written in the Python language and is based on the _Flask_
framework.  Hanmoto works with the PostgreSQL persistence layer and
may work with others (but this is not tested).

The database schema for Hanmoto is based in part upon a schema
originally by [The Code Blogger][0], originally written for the
.NET Framework.  I have adapted this schema to my needs and to
Flask, Postgres, and SQLAlchemy.

Hanmoto's former name is WillPress.  I wanted a name that is less
egotistical.  _Hanmoto_ (版元) is the Japanese word for "publisher."

[0]: https://thecodeblogger.com/2021/06/25/database-schema-for-blog-management-using-net-ef-core/
