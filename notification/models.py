from django.db import models

from account.models import CustomUser
from analogs.models import AnalogProduct


class Notification(models.Model):
    user = models.ForeignKey(CustomUser, models.CASCADE, "notifications")
    product = models.ForeignKey(AnalogProduct, models.CASCADE, "notifications")


class TimeNotification(models.Model):
    set = models.ForeignKey(Notification, models.CASCADE, "times")
    time = models.TimeField()
