import json

from django import forms
from django.db import transaction

from analogs.models import AnalogsSet, AnalogProduct


class AnalogsSetForm(forms.ModelForm):
    def __init__(self, user=None, *args, **kwargs):
        self.user = user
        super(AnalogsSetForm, self).__init__(*args, **kwargs)

    def save_analogs(self, analog_set):
        print(self.data.getlist('products')[0])
        for product in json.loads(self.data.getlist('products')[0]):
            print(product)
            form = AnalogProductsForm(analog_set, product)
            if form.is_valid():
                form.save()
            else:
                raise Exception(form.errors)

    def save(self, commit=True):
        with transaction.atomic():
            self.instance.user = self.user
            analog_set = super(AnalogsSetForm, self).save(commit=commit)
            analog_set.analogs.all().delete()
            self.save_analogs(analog_set)
            return analog_set

    class Meta:
        model = AnalogsSet
        fields = ()


class AnalogProductsForm(forms.ModelForm):
    def __init__(self, analog_set=None, *args, **kwargs):
        self.set = analog_set
        super(AnalogProductsForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        with transaction.atomic():
            self.instance.set = self.set
            return super(AnalogProductsForm, self).save(commit=commit)

    class Meta:
        """
            set = models.ForeignKey(AnalogsSet, models.CASCADE, "analogs")
    product = models.ForeignKey(Product, models.CASCADE, "as_analog")
    type = models.CharField(max_length=16, choices=ANALOG_TYPES, default=ANALOG_TYPES[0][0])
    number_of_times = models.IntegerField()
    reception_time = models.CharField(max_length=16, choices=RECEPTION_TIMES, default=RECEPTION_TIMES[0][0])
    pieces_at_time = models.IntegerField()
    date_start = models.DateField()
    date_end = models.DateField()
    text = models.TextField()
        """
        model = AnalogProduct
        exclude = ('id', 'set', )
