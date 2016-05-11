# Celery client example: request for two numbers multiplication
from celery import Celery

# RabbitMQ
#app = Celery('tasks', broker='amqp://guest@localhost//', backend='amqp')
# Redis
app = Celery('tasks', broker='amqp://ggsister:ggsister@10.151.43.230//', backend='amqp://ggsister:ggsister@10.151.43.230//')

promise = app.send_task('tasks.add', args=[2, 2])

print(promise.get())