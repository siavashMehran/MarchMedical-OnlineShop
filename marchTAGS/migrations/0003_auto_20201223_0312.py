# Generated by Django 3.1.1 on 2020-12-22 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marchTAGS', '0002_auto_20201223_0310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.CharField(blank=True, max_length=80),
        ),
    ]