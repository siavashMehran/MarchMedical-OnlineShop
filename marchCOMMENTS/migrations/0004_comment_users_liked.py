# Generated by Django 3.1.5 on 2021-02-17 00:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('marchCOMMENTS', '0003_auto_20210214_1918'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='users_liked',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]