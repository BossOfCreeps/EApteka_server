from django.urls import path

from analogs.views import Test

urlpatterns = [
    path('analog', Test.as_view()),

]
