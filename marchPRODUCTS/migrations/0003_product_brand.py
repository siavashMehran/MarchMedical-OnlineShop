# Generated by Django 3.1.1 on 2020-11-29 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marchPRODUCTS', '0002_product_caption'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.TextField(blank=True, null=True),
        ),
    ]