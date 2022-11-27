# Generated by Django 3.2.15 on 2022-11-27 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_alter_product_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='unit',
            field=models.CharField(choices=[('м', 'м'), ('шт', 'шт'), ('кг', 'кг')], max_length=10, verbose_name='Еденица измерения'),
        ),
    ]