# Generated by Django 3.2.15 on 2023-03-16 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0034_alter_product_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='unit',
            field=models.CharField(choices=[('кг', 'кг'), ('шт', 'шт'), ('м', 'м')], max_length=10, verbose_name='Еденица измерения'),
        ),
    ]