# Generated by Django 3.1.2 on 2021-11-03 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0008_remove_car_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carmodel',
            old_name='name',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='calculator',
            name='credit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='cars.credit'),
        ),
        migrations.AlterField(
            model_name='credit',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='credit', to='cars.carmodel'),
        ),
    ]
