import os
import django
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop.settings')
django.setup()
app = Celery('shop')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    'send_spam_from_shop': {
        'task': 'applications.spam.tasks.spam_email',
        'schedule': crontab(minute='*/5')
    }
}