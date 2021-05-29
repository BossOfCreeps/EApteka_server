from rest_framework.response import Response
from rest_framework.views import APIView

from account.models import CustomUser
from analogs.forms import AnalogsSetForm
from analogs.models import ANALOG_TYPES, RECEPTION_TIMES
from catalog.models import BaseProduct, Ingredient
from catalog.serializers import BaseProductSerializer, IngredientSerializer


class ProductsByName(APIView):
    # authentication_classes = [CustomAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        products = BaseProduct.objects.filter(name__icontains=request.GET.get("q"))
        return Response({"products": [BaseProductSerializer(product).data for product in products],
                         "ingredients": [IngredientSerializer(ing).data for ing in Ingredient.objects.all()]})


class DropDownValues(APIView):
    # authentication_classes = [CustomAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"types": ANALOG_TYPES,
                         "times": RECEPTION_TIMES})


class Add(APIView):
    # authentication_classes = [CustomAuthentication]
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        form = AnalogsSetForm(CustomUser.objects.first(), request.POST, instance=None)
        if form.is_valid():
            form.save()
        return Response()
