from django.db import models

from account.models import CustomUser
from catalog.models import Product, Order

ANALOG_TYPES = [
    ("inactive", 'Неактивен'),
    ("set", 'Выбран'),
    ("unset", 'Невыбран'),
]

RECEPTION_TIMES = [
    ("before_eating", 'До еды'),
    ("after_eating", 'После еды'),
    ("while_eating", 'Во время'),
    ("empty_stomach", 'На тощак'),
    ("at_any", 'В любое'),
]


class AnalogsSet(models.Model):
    user = models.ForeignKey(CustomUser, models.CASCADE, "analogs_set", null=True, blank=True)
    datetime = models.DateTimeField(auto_now=True)
    order = models.ForeignKey(Order, models.CASCADE, "analogs_set", null=True, blank=True)


class AnalogProduct(models.Model):
    set = models.ForeignKey(AnalogsSet, models.CASCADE, "analogs")
    product = models.ForeignKey(Product, models.CASCADE, "as_analog")
    type = models.CharField(max_length=16, choices=ANALOG_TYPES, default=ANALOG_TYPES[0][0])
    number_of_times = models.IntegerField()
    reception_time = models.CharField(max_length=16, choices=RECEPTION_TIMES, default=RECEPTION_TIMES[0][0])
    pieces_at_time = models.IntegerField()
    date_start = models.DateField()
    date_end = models.DateField()
    text = models.TextField()
