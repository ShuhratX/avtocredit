# Generated by Django 3.1.2 on 2021-10-31 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0007_auto_20211031_1651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='name',
        ),
    ]
