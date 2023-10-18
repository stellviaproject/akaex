from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'base.settings_dev')

app = Celery('base')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


app.conf.beat_schedule = {
     # Everyday at 20:30
    "backup": {
        "task": "core.tasks.backup",
        "schedule": crontab(hour=20, minute=30)
    },
     # Every Monday at 20:30
    "mediabackup": {
        "task": "core.tasks.mediabackup",
        "schedule": crontab(hour=20, minute=30, day_of_week=1),
        "enabled": False
    },
}