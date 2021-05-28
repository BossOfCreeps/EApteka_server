from rest_framework.authentication import BaseAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication as JWT_auth


class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        return JWT_auth().get_user(JWT_auth().get_validated_token(request.META.get('HTTP_AUTHORIZATION'))), None
