# Generated by Django 3.1.2 on 2021-11-06 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0015_remove_credit_month'),
    ]

    operations = [
        migrations.AddField(
            model_name='credit',
            name='month',
            field=models.PositiveIntegerField(default=12),
        ),
    ]
