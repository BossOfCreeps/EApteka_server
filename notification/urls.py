from django.urls import path

from notification import views

urlpatterns = [
    path('/day_notification', views.DayNotification.as_view()),
    path('/create_notification', views.CreateNotification.as_view()),
]
