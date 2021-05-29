from django.db import models

from account.models import CustomUser
from catalog.models import Product, Order, ApplicationMethod

ANALOG_TYPES = [
    ("inactive", 'Неактивен'),
    ("selected", 'Выбран'),
    ("unselected", 'Невыбран'),
]

RECEPTION_TIMES = [
    ("before_eating", 'До еды'),
    ("after_eating", 'После еды'),
    ("while_eating", 'Во время'),
    ("empty_stomach", 'На тощак'),
    ("at_any", 'В любое'),
]


class AnalogsSet(models.Model):
    user = models.ForeignKey(CustomUser, models.CASCADE, "analogs_sets", null=True, blank=True)
    datetime = models.DateTimeField(auto_now=True)
    order = models.ForeignKey(Order, models.CASCADE, "analogs_sets", null=True, blank=True)
    number_of_times = models.IntegerField("Колличество в день", null=True, blank=True)
    days = models.IntegerField("Продолжительность дней приёма", default=0)
    reception_method = models.ForeignKey(ApplicationMethod, models.CASCADE, "analogs_sets", verbose_name="Способ приёма", null=True, blank=True)
    reception_time = models.CharField("В зависимости от еды", max_length=16, choices=RECEPTION_TIMES, default="at_any")
    dosage = models.CharField("Дозировка", null=True, blank=True, max_length=256)
    text = models.TextField(null=True, blank=True)


class AnalogProduct(models.Model):
    set = models.ForeignKey(AnalogsSet, models.CASCADE, "analogs")
    product = models.ForeignKey(Product, models.CASCADE, "as_analog")
    type = models.CharField(max_length=16, choices=ANALOG_TYPES, default=ANALOG_TYPES[0][0])


class AnalogProductFile(models.Model):
    file = models.FileField()
    analog_set = models.ForeignKey(AnalogsSet, models.CASCADE, "files")
