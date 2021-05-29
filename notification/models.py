from datetime import timedelta as td

from django.db import models
from django_celery_beat.models import PeriodicTask

from account.models import CustomUser
from analogs.models import AnalogProduct


class Notification(models.Model):
    product = models.OneToOneField(AnalogProduct, models.CASCADE, null=True)
    date_start = models.DateField(null=True)


class TimeNotification(models.Model):
    set = models.ForeignKey(Notification, models.CASCADE, "times")
    time = models.TimeField()
    celery = models.OneToOneField(PeriodicTask, models.CASCADE, null=True)

    def active(self, date):
        return not (date < self.set.date_start or date > self.set.date_start + td(days=self.set.product.set.days - 1))
