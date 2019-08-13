import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celeryy.settings')

app = Celery('celeryy')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
