# Generated by Django 3.2.15 on 2023-02-06 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0033_alter_product_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='unit',
            field=models.CharField(choices=[('м', 'м'), ('кг', 'кг'), ('шт', 'шт')], max_length=10, verbose_name='Еденица измерения'),
        ),
    ]
