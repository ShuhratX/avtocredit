# Generated by Django 3.1.2 on 2021-11-06 04:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0014_auto_20211106_0909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='credit',
            name='month',
        ),
    ]
