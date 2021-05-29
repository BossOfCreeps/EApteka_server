from rest_framework.response import Response
from rest_framework.views import APIView

from account.models import CustomUser
from analogs.forms import AnalogsSetForm
from analogs.models import ANALOG_TYPES, RECEPTION_TIMES, AnalogsSet, AnalogProduct
from catalog.models import BaseProduct, Ingredient
from catalog.serializers import BaseProductSerializer, IngredientSerializer, BaseProductPlusSerializer
from analogs.serializers import AnalogsSetSerializer


class AnalogsSetAll(APIView):
    # authentication_classes = [CustomAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response([AnalogsSetSerializer(set_).data for set_ in CustomUser.objects.first().analogs_sets.all()])


class AnalogsSetPage(APIView):
    # authentication_classes = [CustomAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(AnalogsSetSerializer(AnalogsSet.objects.get(id=request.GET.get("set_id"))).data)


class AnalogsSelect(APIView):
    # authentication_classes = [CustomAuthentication]
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        selected_analog = AnalogProduct.objects.get(id=request.POST.get("analog_product_id"))
        for set_analog in selected_analog.set.analogproducts.all():
            set_analog.type = "selected" if set_analog == selected_analog else "unselected"
            set_analog.save()
        return Response()


class ProductsByName(APIView):
    # authentication_classes = [CustomAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        products = BaseProduct.objects.filter(name__icontains=request.GET.get("q"))
        return Response({"products": [BaseProductSerializer(product).data for product in products],
                         "ingredients": [IngredientSerializer(ing).data for ing in Ingredient.objects.all()]})


class AnalogListByIngredient(APIView):
    # authentication_classes = [CustomAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(
            BaseProductPlusSerializer(BaseProduct.objects.get(ingredient_id=request.GET.get("ingredient_id"))).data)


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
