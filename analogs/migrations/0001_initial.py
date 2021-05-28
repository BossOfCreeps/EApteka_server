# Generated by Django 3.2.3 on 2021-05-28 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnalogsSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analogs_set', to='catalog.order')),
            ],
        ),
        migrations.CreateModel(
            name='AnalogProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('inactive', 'Неактивен'), ('set', 'Выбран'), ('unset', 'Невыбран')], default='inactive', max_length=16)),
                ('number_of_times', models.IntegerField()),
                ('reception_time', models.CharField(choices=[('before_eating', 'До еды'), ('after_eating', 'После еды'), ('while_eating', 'Во время'), ('empty_stomach', 'На тощак'), ('at_any', 'В любое')], default='before_eating', max_length=16)),
                ('pieces_at_time', models.IntegerField()),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('text', models.TextField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='as_analog', to='catalog.product')),
                ('set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analogs', to='analogs.analogsset')),
            ],
        ),
    ]