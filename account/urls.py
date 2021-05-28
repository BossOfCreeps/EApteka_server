from django.contrib import admin
from django.urls import path

from account.views import SignIn

urlpatterns = [
    path('/sign_in', SignIn.as_view()),
]
