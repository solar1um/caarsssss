# Generated by Django 3.2.6 on 2021-08-14 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0010_alter_car_power'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='type',
            field=models.CharField(blank=True, choices=[('new', 'new'), ('user', 'user')], max_length=5, null=True),
        ),
    ]