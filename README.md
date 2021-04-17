# Exponetial-backoff-flask
# This is a simple exponential backoff application using arithmetic logic. <br/>
Create Python3 env and install the packages in requirements.txt <br/>
Install Redis server <code>sudo apt install redis-server</code> <br/>
Run the celery task <code>celery -A app.celery worker --loglevel=info</code> <br/>
Run the Flask application <code>python3 app.py</code>
