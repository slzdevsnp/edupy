#!/bin/sh
export FLASK_APP=./cashman/index.py
# --debug is for development mode
# -h 0.0.0.0  listen to all network interfaces
pipenv run flask  --debug run -h 0.0.0.0


