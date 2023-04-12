# Generated by Django 4.2 on 2023-04-12 12:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('age', models.PositiveIntegerField(validators=[django.core.validators.MinLengthValidator(13), django.core.validators.MaxLengthValidator(19)])),
                ('sex', models.PositiveIntegerField(choices=[(0, 'Female'), (1, 'Male')], null=True)),
            ],
        ),
    ]
