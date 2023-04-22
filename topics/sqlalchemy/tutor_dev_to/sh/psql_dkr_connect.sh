#!/usr/bin/env bash

# docker container with postgres must be running

USER=learner
USERPWD=StrongPassword123
DBNAME=learnsqlalchemy
PGPASSWORD=${USERPWD} psql --host localhost --username ${USER} --dbname ${DBNAME}
