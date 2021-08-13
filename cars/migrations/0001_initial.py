# Generated by Django 3.2.6 on 2021-08-12 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('model', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name_plural': 'Brand',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriptions', models.TextField(max_length=400)),
                ('volume', models.FloatField()),
                ('price', models.PositiveIntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='ads')),
                ('release_date', models.DateField()),
                ('color', models.CharField(max_length=20)),
                ('transmission', models.CharField(blank=True, choices=[('automatic', 'automatic'), ('manual', 'manual'), ('CVT', 'CVT'), ('SMG', 'SMG')], max_length=20, null=True)),
                ('rul', models.CharField(blank=True, choices=[('left', 'left'), ('right', 'right')], max_length=6, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]