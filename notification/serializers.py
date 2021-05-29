from rest_framework import serializers

from analogs.serializers import AnalogProductSerializer
from notification.models import TimeNotification, Notification


class NotificationSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    product = AnalogProductSerializer()
    date_start = serializers.DateField()

    class Meta:
        model = Notification
        fields = ["id", "product", "date_start"]


class TimeNotificationSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    time = serializers.TimeField(format="%H:%M")
    set = NotificationSerializer()

    class Meta:
        model = TimeNotification
        fields = ["id", "time", "set"]