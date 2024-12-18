# Generated by Django 5.1.1 on 2024-12-12 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('starting_point', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('start_lat', models.FloatField()),
                ('start_lon', models.FloatField()),
                ('end_lat', models.FloatField()),
                ('end_lon', models.FloatField()),
                ('stops', models.TextField()),
            ],
        ),
    ]
