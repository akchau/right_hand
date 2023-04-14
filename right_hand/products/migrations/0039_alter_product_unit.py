# Generated by Django 3.2.15 on 2023-04-12 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0038_alter_product_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='unit',
            field=models.CharField(choices=[('м', 'м'), ('шт', 'шт'), ('кг', 'кг')], max_length=10, verbose_name='Еденица измерения'),
        ),
    ]
