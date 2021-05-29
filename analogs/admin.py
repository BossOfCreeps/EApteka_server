from django.contrib import admin

from analogs.models import AnalogsSet, AnalogProduct, AnalogProductFile

admin.site.register(AnalogsSet)
admin.site.register(AnalogProduct)
admin.site.register(AnalogProductFile)
