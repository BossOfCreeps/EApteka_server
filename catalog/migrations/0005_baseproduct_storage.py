# Generated by Django 3.2.3 on 2021-05-29 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_order_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseproduct',
            name='storage',
            field=models.TextField(blank=True, null=True),
        ),
    ]