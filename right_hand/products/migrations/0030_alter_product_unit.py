# Generated by Django 3.2.15 on 2023-02-03 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0029_alter_product_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='unit',
            field=models.CharField(choices=[('кг', 'кг'), ('м', 'м'), ('шт', 'шт')], max_length=10, verbose_name='Еденица измерения'),
        ),
    ]
