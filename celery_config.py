from kombu import Exchange, Queue
from datetime import timedelta

BROKER_URL = "redis://192.168.0.107:6379/0"
CELERY_RESULT_BACKEND = "redis://192.168.0.107:6379/0"
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_ENABLE_UTC = True
CELERY_TIMEZONE = "UTC"
CELERY_DEFAULT_QUEUE = "default"
CELERY_QUEUES = (
    Queue("default", Exchange("default"), routing_key="default"),
)

# Celery Beat Configuration
CELERYBEAT_SCHEDULE = {
    'get_nifty_stocks': {
        'task': 'tasks.get_nifty_data',
        'schedule': timedelta(seconds=45),  # Adjust the schedule as needed
    },
    'get_nasdaq_stocks': {
        'task': 'tasks.get_nasdaq_data',
        'schedule': timedelta(seconds=90),  # Adjust the schedule as needed
    },
}
