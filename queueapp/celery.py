import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'queueapp.settings')

app = Celery('queueapp')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
