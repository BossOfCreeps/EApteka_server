from rest_framework import serializers

from account.serializers import UserSerializer
from catalog.models import Product, BaseProduct, Order, OrderProduct


class IngredientSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField()

    class Meta:
        model = BaseProduct
        fields = ['id', 'name']


class BaseProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    ingredient = IngredientSerializer()
    form = serializers.CharField()
    application_method = serializers.CharField()

    class Meta:
        model = BaseProduct
        fields = ['id', 'name', 'ingredient', 'form', 'application_method']


class ProductSerializer(serializers.ModelSerializer):
    base = BaseProductSerializer()
    size = serializers.CharField()
    price = serializers.FloatField()
    text = serializers.CharField()
    img = serializers.ImageField()

    class Meta:
        model = Product
        fields = ['base', 'size', 'price', 'text', 'img']


class BaseProductPlusSerializer(BaseProductSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = BaseProduct
        fields = ['id', 'name', 'ingredient', 'form', 'application_method', 'products']


class OrderProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    count = serializers.IntegerField()

    class Meta:
        model = OrderProduct
        fields = ['product', "count"]


class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    datetime = serializers.DateTimeField()
    type = serializers.CharField()
    order_products = OrderProductSerializer(many=True)

    class Meta:
        model = Order
        fields = ['user', 'datetime', 'type', 'order_products']
