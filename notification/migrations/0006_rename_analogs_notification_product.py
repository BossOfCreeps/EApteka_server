# Generated by Django 3.2.3 on 2021-05-29 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0005_alter_notification_analogs'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='analogs',
            new_name='product',
        ),
    ]
