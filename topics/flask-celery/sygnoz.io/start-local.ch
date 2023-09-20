export FLASK_DEBUG=1

export FLASK_RUN_HOST=0.0.0.0
export FLASK_RUN_PORT=5001

celery -A app.celery worker --concurrency=50 --loglevel=INFO  2>&1 | tee /tmp/celery.log  &

python -m flask run

# to kill celery procesees  :  killall celery 