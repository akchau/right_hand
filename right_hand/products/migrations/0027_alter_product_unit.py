# Generated by Django 3.2.15 on 2023-01-05 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_alter_product_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='unit',
            field=models.CharField(choices=[('шт', 'шт'), ('м', 'м'), ('кг', 'кг')], max_length=10, verbose_name='Еденица измерения'),
        ),
    ]
