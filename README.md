# WillPress

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/dfbc8f722a5e4eef81e8f35c8ee1f206)](https://www.codacy.com/gh/waellison/willpress/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=waellison/willpress&amp;utm_campaign=Badge_Grade)
[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/dfbc8f722a5e4eef81e8f35c8ee1f206)](https://www.codacy.com/gh/waellison/willpress/dashboard?utm_source=github.com&utm_medium=referral&utm_content=waellison/willpress&utm_campaign=Badge_Coverage)
[![build](https://github.com/waellison/willpress/actions/workflows/pytest.yml/badge.svg)](https://github.com/waellison/willpress/actions/workflows/pytest.yml)
[![CodeQL](https://github.com/waellison/willpress/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/waellison/willpress/actions/workflows/codeql-analysis.yml)
[![License](https://img.shields.io/github/license/waellison/willpress)](#)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

_WillPress_ is a blog engine.  It is designed to expose a REST API that
can be consumed by a mobile client, SPA frontend, or any other client
software that can communicate in JSON.

WillPress is written in the Python language and is based on the _Flask_
framework.  WillPress works with the PostgreSQL persistence layer and
may work with others (but this is not tested).

The database schema for WillPress is based in part upon a schema
originally by [The Code Blogger][0], originally written for the
.NET Framework.  I have adapted this schema to my needs and to
Flask, Postgres, and SQLAlchemy.

[0]: https://thecodeblogger.com/2021/06/25/database-schema-for-blog-management-using-net-ef-core/
