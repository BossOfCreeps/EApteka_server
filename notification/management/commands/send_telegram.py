from django.core.management.base import BaseCommand

from account.models import CustomUser
from catalog.models import Order
from notification.bot import tg_notification, tg_storage_rules
from notification.models import TimeNotification


class Command(BaseCommand):
    def handle(self, *args, **options):
        tg_notification(CustomUser.objects.first(), TimeNotification.objects.first())
