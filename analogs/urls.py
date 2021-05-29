from django.urls import path

from analogs import views

urlpatterns = [
    # all analogs set page
    path('/all', views.AnalogsSetAll.as_view()),
    # analogs set page
    path('/set', views.AnalogsSetPage.as_view()),
    path('/select_analog', views.AnalogsSelect.as_view()),
    # add analogs page
    path('/products_by_name', views.ProductsByName.as_view()),
    path('/list_by_ingredient', views.AnalogListByIngredient.as_view()),
    path('/drop_down_values', views.DropDownValues.as_view()),
    path('/add', views.Add.as_view()),
]
