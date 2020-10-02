from celery_app import .app


@app.task
def add(x, y):
    sleep(30)
    return x + y
