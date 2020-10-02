from celery import Celery
from time import sleep

app = Celery('tasks', backend='rpc://', broker='amqp://localhost')
# where does rpc:// live and why?

@app.task
def add(x, y):
    sleep(30)
    return x + y
