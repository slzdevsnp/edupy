#!/bin/sh

#source ~/venv/eduflask/bin/activate

export FLASK_APP=./cashman/index.py
# --debug is for development mode
# -h 0.0.0.0  listen to all network interfaces

python -m flask  --debug run -h 0.0.0.0


