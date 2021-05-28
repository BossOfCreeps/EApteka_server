from rest_framework import serializers

from analogs.models import AnalogsSet
"""

class AnalogProductSerializer(serializers.ModelSerializer):

        set = models.ForeignKey(AnalogsSet, models.CASCADE, "analogs")
    product = models.ForeignKey(Product, models.CASCADE, "as_analog")
    type = models.CharField(max_length=16, choices=ANALOG_TYPES, default=ANALOG_TYPES[0][0])
    number_of_times = models.IntegerField()
    reception_time = models.CharField(max_length=16, choices=RECEPTION_TIMES, default=RECEPTION_TIMES[0][0])
    pieces_at_time = models.IntegerField()
    date_start = models.DateField()
    date_end = models.DateField()
    text = models.TextField()

    product = ProductSerializer()
    type = serializers.CharField()
    analogs = AnalogProductSerializer()

    class Meta:
        model = AnalogsSet
        exclude = ('set', )


class UserSerializer(serializers.ModelSerializer):
    datetime = serializers.DateTimeField()
    order = OrderSerializer()
    analogs = AnalogProductSerializer(multiple=True)

    class Meta:
        model = AnalogsSet
        fields = ['datetime', 'email', 'profile']
"""