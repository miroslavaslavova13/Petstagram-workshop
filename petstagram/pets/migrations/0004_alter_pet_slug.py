# Generated by Django 3.2.16 on 2022-10-16 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0003_pet_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]