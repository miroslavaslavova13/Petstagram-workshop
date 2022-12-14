# Generated by Django 3.2.16 on 2022-11-10 18:22

import django.core.validators
from django.db import migrations, models
import petstagram.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petstagramuser',
            name='first_name',
            field=models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2), petstagram.core.validators.validate_only_letters]),
        ),
        migrations.AlterField(
            model_name='petstagramuser',
            name='last_name',
            field=models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2), petstagram.core.validators.validate_only_letters]),
        ),
    ]
