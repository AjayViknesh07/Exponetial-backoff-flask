from flask import Flask, request, render_template
from celery import Celery
import requests

app = Flask(__name__)

# Updating the Flask app configurations fro celery
app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',
)
# Initiating Celery
celery = Celery(app.name,broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

''' Creating a Celery task with maximum retry of 3 times.
    Also this task has an exponential backoff login implemented in it.
    This task will retry exponentially based on the number of retires '''
@celery.task(bind=True,max_retries=3)
def exponential_logic(self,a,b):
    try:
        c = a/b
    except Exception as exc:
        '''The task will retry if an exception arise and with a countdown using exponential backoff logic'''
        self.retry(exc=exc, countdown=1 ** self.request.retries)
    return a+b

# Created a demo controller to execute the celery task.
@app.route('/', methods=['GET'])
def index():
    # Initiating the celery task and passing the values as parameters
    status = exponential_logic.delay(5,0)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)