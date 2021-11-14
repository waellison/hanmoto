-- init for the uchapishaji database.

drop database if exists uchapishaji;

create database uchapishaji;

\c uchapishaji

set statement_timeout = 0;
set lock_timeout = 0;
set client_encoding = 'UTF8';
set standard_conforming_strings = on;
set check_function_bodies = false;
set client_min_messages = warning;
set default_tablespace = '';
set default_with_oids = false;

