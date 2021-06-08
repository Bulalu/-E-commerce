import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'keikoo.settings')

app = Celery('keikoo')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()