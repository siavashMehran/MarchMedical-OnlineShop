# Generated by Django 3.1.5 on 2021-02-14 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marchCOMMENTS', '0002_auto_20210214_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.CharField(max_length=50),
        ),
    ]
