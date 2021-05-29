from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password, **extra_fields):
        username = self.normalize_email(username)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(username, password, **extra_fields)


class CustomUser(AbstractUser):
    username = models.CharField("Имя", max_length=255, unique=True)
    telegram_id = models.IntegerField("Telegram ID", blank=True, null=True)

    first_name = None
    last_name = None
    groups = None
    user_permissions = None
    last_login = None
    date_joined = None

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.username}"

    class Meta:
        verbose_name = verbose_name_plural = "Кастомный пользователь"
