from django.db import models

from account.models import CustomUser
from analogs.models import AnalogProduct


class Notification(models.Model):
    product = models.ForeignKey(AnalogProduct, models.CASCADE, "notifications", null=True, blank=True)


class TimeNotification(models.Model):
    set = models.ForeignKey(Notification, models.CASCADE, "times")
    time = models.TimeField()
