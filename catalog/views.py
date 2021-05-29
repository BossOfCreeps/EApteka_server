from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from catalog.models import BaseProduct, Ingredient
from account.authentication import CustomAuthentication
from catalog.serializers import BaseProductSerializer,IngredientSerializer
