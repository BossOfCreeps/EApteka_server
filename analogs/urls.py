from django.urls import path

from analogs import views

urlpatterns = [
    path('/products_by_name', views.ProductsByName.as_view()),
    path('/drop_down_values', views.DropDownValues.as_view()),
    path('/add', views.Add.as_view()),
]
