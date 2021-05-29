import json

from django import forms
from django.db import transaction

from analogs.models import AnalogsSet, AnalogProduct, AnalogProductFile


class AnalogsSetForm(forms.ModelForm):
    def __init__(self, user=None, *args, **kwargs):
        self.user = user
        super(AnalogsSetForm, self).__init__(*args, **kwargs)

    def save_analogs(self, analog_set):
        for product in json.loads(self.data.getlist('products')[0]):
            form = AnalogProductsForm(analog_set, product)
            if form.is_valid():
                form.save()
            else:
                raise Exception(form.errors)

    def save_files(self, analog_set):
        for file in self.files.getlist('files'):
            AnalogProductFile.objects.create(file=file, analog_set=analog_set)

    def save(self, commit=True):
        with transaction.atomic():
            self.instance.user = self.user
            analog_set = super(AnalogsSetForm, self).save(commit=commit)
            analog_set.analogs.all().delete()
            self.save_analogs(analog_set)
            self.save_files(analog_set)
            return analog_set

    class Meta:
        model = AnalogsSet
        exclude = ('id', 'user', 'order', 'datetime',)


class AnalogProductsForm(forms.ModelForm):
    def __init__(self, analog_set=None, *args, **kwargs):
        self.set = analog_set
        super(AnalogProductsForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        with transaction.atomic():
            self.instance.set = self.set
            analog_product = super(AnalogProductsForm, self).save(commit=commit)
            return analog_product

    class Meta:
        model = AnalogProduct
        exclude = ('id', 'set',)
