-- init for the willpress database.

drop database if exists willpress;

create database willpress;

\c willpress

set statement_timeout = 0;
set lock_timeout = 0;
set client_encoding = 'UTF8';
set standard_conforming_strings = on;
set check_function_bodies = false;
set client_min_messages = warning;
set default_tablespace = '';
set default_with_oids = false;

