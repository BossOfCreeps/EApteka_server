from django.db import models

from account.models import CustomUser


class Ingredient(models.Model):
    name = models.CharField(max_length=512)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = verbose_name_plural = "Действующее вещество"


class Form(models.Model):
    name = models.CharField(max_length=512)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = verbose_name_plural = "Форма"


class ApplicationMethod(models.Model):
    name = models.CharField(max_length=512)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = verbose_name_plural = "Способ применения"


class Size(models.Model):
    name = models.CharField(max_length=512)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = verbose_name_plural = "Размер"


class BaseProduct(models.Model):
    name = models.CharField(max_length=512)
    ingredient = models.ForeignKey(Ingredient, models.CASCADE, "base_products")
    form = models.ForeignKey(Form, models.CASCADE, "base_products")
    application_method = models.ForeignKey(ApplicationMethod, models.CASCADE, "base_products")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = verbose_name_plural = "Базовый продукт"


class Product(models.Model):
    base = models.ForeignKey(BaseProduct, models.CASCADE, "products")
    size = models.ForeignKey(Size, models.CASCADE, "products")
    price = models.FloatField("Цена")
    text = models.TextField()
    img = models.ImageField(blank=True, null=True)

    def __str__(self):
        return f"{self.base} {self.size} {self.price}"

    class Meta:
        verbose_name = verbose_name_plural = "Продукт"


ORDER_TYPE = [
    ("basket", 'В корзине'),
    ("purchased", 'Куплено'),
]


class Order(models.Model):
    user = models.ForeignKey(CustomUser, models.CASCADE, "orders")
    datetime = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=16, choices=ORDER_TYPE, default="basket")


class OrderProduct(models.Model):
    product = models.ForeignKey(Product, models.CASCADE, "order_products")
    order = models.ForeignKey(Order, models.CASCADE, "order_products")
    count = models.IntegerField(default=0)
