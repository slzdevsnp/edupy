#!/usr/bin/env bash

# docker container with postgres must be running

PGPASSWORD=password psql --host localhost --username postgres --dbname postgres
