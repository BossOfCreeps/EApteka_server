# Generated by Django 3.2.3 on 2021-05-29 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0009_auto_20210529_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='date_start',
            field=models.DateField(null=True),
        ),
    ]
