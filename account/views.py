from django.contrib.auth import authenticate
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken


class SignIn(APIView):
    def post(self, request):
        user = authenticate(username=request.POST["username"], password=request.POST["password"])
        if user is not None:
            token = RefreshToken.for_user(user)
            return Response({'refresh': str(token), 'access': str(token.access_token)})
        else:
            raise Http404()

