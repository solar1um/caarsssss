# Generated by Django 3.2.6 on 2021-08-13 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_remove_brand_model'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='descriptions',
            new_name='description',
        ),
    ]