from rest_framework.response import Response
from rest_framework.views import APIView

from catalog.models import Order
from catalog.serializers import OrderSerializer


class Test(APIView):
    #authentication_classes = [CustomAuthentication]
    #permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"status": OrderSerializer(Order.objects.first()).data})
