# Generated by Django 3.1.2 on 2021-11-06 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0011_auto_20211104_1157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calculator',
            name='month',
        ),
        migrations.RemoveField(
            model_name='credit',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='credit',
            name='first_payment',
        ),
    ]