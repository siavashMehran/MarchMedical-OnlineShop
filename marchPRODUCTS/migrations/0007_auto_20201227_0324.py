# Generated by Django 3.1.1 on 2020-12-26 23:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('marchCATEGORIES', '0002_auto_20201227_0324'),
        ('marchPRODUCTS', '0006_auto_20201225_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(blank=True, to='marchCATEGORIES.Category', verbose_name='دسته'),
        ),
        migrations.AddField(
            model_name='product',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='تاریخ و ساعت'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='caption',
            field=models.CharField(max_length=160, verbose_name='توضیحات کوتاه و مختصر'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=800, verbose_name=' توضیح کامل'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(default=0, verbose_name='قیمت'),
        ),
    ]
