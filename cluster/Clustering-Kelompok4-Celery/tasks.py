# Celery service example: task to multiply two numbers
from celery import Celery

# RabbitMQ
#app = Celery('tasks', broker='amqp://guest@localhost//', backend='amqp')
# Redis
app = Celery('tasks', broker='amqp://ggsister:ggsister@10.151.43.230//', backend='amqp://ggsister:ggsister@10.151.43.230//')

@app.task
def multiply(a, b):
    return a * b