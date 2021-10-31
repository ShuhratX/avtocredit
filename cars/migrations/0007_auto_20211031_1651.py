# Generated by Django 3.1.2 on 2021-10-31 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0006_auto_20211029_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='complectation',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='credit',
            name='complectation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.car'),
        ),
        migrations.DeleteModel(
            name='Complectation',
        ),
    ]
