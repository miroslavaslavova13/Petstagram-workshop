# Generated by Django 3.2.16 on 2022-11-11 19:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0002_photocomment_photolike'),
    ]

    operations = [
        migrations.AddField(
            model_name='photocomment',
            name='user',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.RESTRICT, to='accounts.petstagramuser'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photolike',
            name='user',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.RESTRICT, to='accounts.petstagramuser'),
            preserve_default=False,
        ),
    ]
