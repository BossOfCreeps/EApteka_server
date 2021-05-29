from rest_framework import serializers

from analogs.models import AnalogsSet, AnalogProduct, AnalogProductFile
from catalog.serializers import OrderSerializer, ProductSerializer


class AnalogProductFileSerializer(serializers.ModelSerializer):
    file = serializers.FileField()

    class Meta:
        model = AnalogProductFile
        fields = ["file", ]


class AnalogProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    type = serializers.CharField()

    class Meta:
        model = AnalogProduct
        exclude = ["set", ]


class AnalogsSetSerializer(serializers.ModelSerializer):
    datetime = serializers.DateTimeField()
    order = OrderSerializer()
    analogs = AnalogProductSerializer(many=True)
    number_of_times = serializers.IntegerField()
    reception_method = serializers.CharField()
    reception_time = serializers.CharField()
    days = serializers.IntegerField()
    dosage = serializers.CharField()
    text = serializers.CharField()
    files = AnalogProductFileSerializer(many=True)

    class Meta:
        model = AnalogsSet
        fields = ["datetime", "order", "analogs", "number_of_times", "days", "reception_method", "reception_time",
                  "days", "dosage", "text", "files"]
