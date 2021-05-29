from datetime import time

from django.core.management.base import BaseCommand
from django.utils.timezone import now
from django_celery_beat.models import PeriodicTask, IntervalSchedule

from notification.models import TimeNotification, Notification


class Command(BaseCommand):
    def handle(self, *args, **options):
        TimeNotification.objects.create(
            set=Notification.objects.first(),
            time=time(hour=15, minute=15),
            celery=PeriodicTask.objects.create(
                name='Call notification',
                task="eapteka.celery.call_notification",
                interval=IntervalSchedule.objects.get_or_create(every=1, period='days')[0],
                start_time=now(),
            )
        )
