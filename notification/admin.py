from django.contrib import admin

from notification.models import Notification, TimeNotification

admin.site.register(Notification)
admin.site.register(TimeNotification)
