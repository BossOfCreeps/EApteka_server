"""
Commands to start
    python3 manage.py start_celery
    celery -A eapteka beat -l INFO
    celery -A eapteka worker -l INFO
"""

import os

from celery import Celery
from django.apps import apps

from eapteka import settings
from notification.bot import tg_notification

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eapteka.settings')

app = Celery('eapteka')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.config_from_object(settings)
app.autodiscover_tasks(lambda: [n.name for n in apps.get_app_configs()])


@app.task(bind=True)
def call_notification(self, product_id):
    from analogs.models import AnalogProduct
    product = AnalogProduct.objects.get(id=product_id)
    tg_notification(product.set.user, product)


@app.task(bind=True)
def test(self):
    print(1)
