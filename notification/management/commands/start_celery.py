from django.core.management.base import BaseCommand
from django.utils.timezone import now
from django_celery_beat.models import PeriodicTask, IntervalSchedule


class Command(BaseCommand):
    def handle(self, *args, **options):
        PeriodicTask.objects.create(
            name='Call notification',
            task="eapteka.celery.call_notification",
            interval=IntervalSchedule.objects.get_or_create(every=10, period='seconds')[0],
            start_time=now(),
        )
