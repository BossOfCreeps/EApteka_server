from datetime import datetime

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from account.authentication import CustomAuthentication
from notification.models import TimeNotification
from notification.serializers import TimeNotificationSerializer


class DayNotification(APIView):
    # authentication_classes = [CustomAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        date = datetime.strptime(request.GET.get("date"), '%d/%m/%Y').date()
        return Response([TimeNotificationSerializer(notification).data
                         for notification in TimeNotification.objects.all() if notification.active(date)])
