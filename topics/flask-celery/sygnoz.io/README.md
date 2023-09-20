flask with celery
=====

# Context
Celery is a scheduler for (long-running) python tasks launched in background. redis is used to cooordinate task identifiers.  in Flask Celery allows to implement async non-blocking apis which launch long executing code in backgound



# tutorial
url: https://signoz.io/blog/celery-worker/

github repo:  https://github.com/EzzEddin/tutorials/tree/master/celery_workers_flask_redis

## env
created new env
```sh
cd ~/venv
python3 -m virtualenv celerybase
. celerybase/bin/activate
pip install --upgrade pip
```

```sh
pip install Flask==2.0.2
pip install celery==5.0.0
pip install redis==4.6.0
```
or create a file in project root `requirements.txt` with content:
```txt
celery==5.0.0
Flask==2.0.2
redis==4.6.0
```
then  `pip install -r requirements.txt`


`pip list`

# redis in docker-compose

create file docker-compose.yml in projecr root with  content
```yaml
version: "3"
services:


  redis:
    image: redis:latest
    container_name: redis_container
    ports:
      - "6379:6379"
    volumes:
      - ~/tmp/redis_data:/data
```

Check if  redis is alredy running in docker with  `docker ps -a`.
If needed kill it with `docker stop uid` , `docker rm uid`

Start docker  in background  `docker-compose up -d`  check its logs with  ` docker-compose logs redis -f`
or in the foreground  `docker-compose up`


# flask app code
In root folder create file `app.py` with contents:
```py
from flask import Flask, jsonify
from celery import Celery

app = Flask(__name__)
app.config["CELERY_BROKER_URL"] = "redis://localhost:6379"

celery = Celery(app.name, broker=app.config["CELERY_BROKER_URL"])
celery.conf.update(app.config)


@celery.task()
def add(x, y):
    return x + y


@app.route('/')
def add_task():
    for i in range(10000):
        add.delay(i, i)
    return jsonify({'status': 'ok'})
```


# start celery and flask

prep a file  `start-local.ch` with contents

```sh
export FLASK_DEBUG=1

export FLASK_RUN_HOST=0.0.0.0
export FLASK_RUN_PORT=5001

celery -A app.celery worker --concurrency=10 --loglevel=INFO  2>&1 | tee /tmp/celery.log  &

python -m flask run
```

start it and then reach   in browser  http://localhost:5001

you will see in the console the celery logs starting 10K simple addition tasks.   The endpoint will return  before 

in my app.py i have modfily app.py  to have endpoints  /submit_tasks  and  /get_sum

you /submit tasks  which returns when all tasks are enqueued,   then in the mean time hit reload /get_sum
multiple times,  you may see partial results of sum, and when all tasks are executed then you will see the final expected total. 