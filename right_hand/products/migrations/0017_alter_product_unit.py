# Generated by Django 3.2.15 on 2022-11-27 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_alter_product_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='unit',
            field=models.CharField(choices=[('шт', 'шт'), ('кг', 'кг'), ('м', 'м')], max_length=10, verbose_name='Еденица измерения'),
        ),
    ]
