from django.contrib import admin

from catalog.models import Ingredient, Form, ApplicationMethod, Size, BaseProduct, Product, Order, OrderProduct

admin.site.register(Ingredient)
admin.site.register(Form)
admin.site.register(ApplicationMethod)
admin.site.register(Size)
admin.site.register(BaseProduct)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderProduct)
