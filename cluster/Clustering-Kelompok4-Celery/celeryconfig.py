# To set these, change the environment variables instead.
CELERY_RESULT_BACKEND = 'amqp://ggsister:ggsister@10.151.43.230//'
BROKER_URL = 'amqp://ggsister:ggsister@10.151.43.230//'

CELERY_TASK_SERIALIZER = 'pickle'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT=['pickle', 'json']
CELERY_TIMEZONE = 'Australia/Sydney'
CELERY_ENABLE_UTC = True
CELERYD_MAX_TASKS_PER_CHILD=1