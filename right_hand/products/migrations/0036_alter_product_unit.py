# Generated by Django 3.2.15 on 2023-04-07 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0035_alter_product_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='unit',
            field=models.CharField(choices=[('шт', 'шт'), ('кг', 'кг'), ('м', 'м')], max_length=10, verbose_name='Еденица измерения'),
        ),
    ]
