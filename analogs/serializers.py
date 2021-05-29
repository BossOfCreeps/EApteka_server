from rest_framework import serializers

from analogs.models import AnalogsSet, AnalogProduct
from catalog.serializers import OrderSerializer, ProductSerializer


class AnalogProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    type = serializers.CharField()
    number_of_times = serializers.IntegerField()
    reception_time = serializers.CharField()
    pieces_at_time = serializers.IntegerField()
    date_start = serializers.DateField()
    date_end = serializers.DateField()
    text = serializers.CharField()

    class Meta:
        model = AnalogProduct
        exclude = ["set",]


class AnalogsSetSerializer(serializers.ModelSerializer):
    datetime = serializers.DateTimeField()
    order = OrderSerializer()
    analogs = AnalogProductSerializer(many=True)

    class Meta:
        model = AnalogsSet
        fields = ["datetime", "order", "analogs"]
