from flask import Flask, jsonify
from celery import Celery
from celery.result import allow_join_result

import time 
from datetime import datetime 

app = Flask(__name__)
app.config["CELERY_BROKER_URL"] = "redis://localhost:6379"
app.config["CELERY_RESULT_BACKEND"] = "redis://localhost:6379"


celery = Celery(app.name, broker=app.config["CELERY_BROKER_URL"])
celery.conf.update(app.config)


def addition(x,y):
    return x + y

@celery.task()
def add(x, y):
    return x + y

task_list = []
dt_submitted = None 

@app.route('/submit_tasks')
def submit_tasks():
    global dt_submitted 
    global task_list
    dt_submitted = datetime.now()
    n_tasks=10000
    task_list = [add.delay(i, i) for i in range(n_tasks)]
    return jsonify({'status': f'{n_tasks} tasks_submitted'})


@app.route('/get_sum')
def get_sum():
    total = 0
    global task_list
    with allow_join_result():
        for task in task_list:
            if task.ready():
                total += task.get()
    return jsonify({'status': 'ok', 'sum': total})


@app.route('/task_status/<task_id>')
def task_status(task_id):
    task = celery.AsyncResult(task_id)
    return jsonify({'task_id': task_id, 'status': task.state})


@app.route('/task_status')
def all_tasks_status():
    global task_list
    global dt_submitted
    result = {'tasks submited': 0 , 'submitted at': dt_submitted }
    for task in task_list:
        result['tasks submited'] = result['tasks submited'] + 1
        result[task.id] = task.state
    return jsonify(result)    




@app.route('/sync')
def add_sync():
    i_max = 10000
    res = 0
    dt_s = datetime.now()
    s_t = time.time()
    for i in range(i_max):
        res += addition(i,i)
    e_t = time.time()
    dt_e = datetime.now()
    delta = e_t - s_t
    return jsonify({'status sync': 'ok', 'result': res , 'dt_start': dt_s, 'dt_end': dt_e, 'exec_time_sec':delta})
