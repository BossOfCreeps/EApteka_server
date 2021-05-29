from datetime import datetime
from random import choices
from string import digits, ascii_uppercase

from django import forms
from django.db import transaction
from django_celery_beat.models import IntervalSchedule, PeriodicTask

from notification.models import Notification, TimeNotification


class NotificationForm(forms.ModelForm):
    def save_times(self, notification):
        for time_ in self.data.getlist('times'):
            date = notification.date_start
            time = datetime.strptime(time_, '%H:%M:%S')
            TimeNotification.objects.create(
                set=notification,
                time=time,
                celery=PeriodicTask.objects.create(
                    name=f'Call notification {"".join(choices(ascii_uppercase + digits, k=100))}',
                    task="eapteka.celery.call_notification",
                    interval=IntervalSchedule.objects.get_or_create(every=1, period='days')[0],
                    start_time=datetime(date.year, date.month, date.day, time.hour, time.minute)
                )
            )

    def save(self, commit=True):
        with transaction.atomic():
            notification = super(NotificationForm, self).save(commit=commit)
            notification.times.all().delete()
            self.save_times(notification)
            return notification

    class Meta:
        model = Notification
        fields = ('product', 'date_start')
