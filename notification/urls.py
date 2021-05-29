from django.urls import path

from notification import views

urlpatterns = [
    path('/day_notification', views.DayNotification.as_view()),
]
