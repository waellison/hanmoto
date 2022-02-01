#!/bin/bash

cat /dev/urandom | LC_ALL=C tr -dc 'a-zA-Z0-9' | fold -w "${1:-30}" | head -n 1

