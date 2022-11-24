# Generated by Django 3.2.15 on 2022-11-19 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Укажите название сборки.', max_length=200, verbose_name='Название сборки.')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Укажите название товара.', max_length=200, verbose_name='Название товара.')),
                ('reference', models.CharField(help_text='Укажите заводской артикул', max_length=50, verbose_name='Артикул производителя.')),
                ('unit', models.CharField(choices=[('м', 'м'), ('шт', 'шт'), ('кг', 'кг')], max_length=10, verbose_name='Еденица измерения.')),
                ('price', models.PositiveIntegerField(verbose_name='Стоимость в прайсе производтеля.')),
            ],
        ),
        migrations.CreateModel(
            name='ProductsCollection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numbers', models.PositiveIntegerField(help_text='Укажите количество.', verbose_name='Количество элементов в сборке')),
                ('collection', models.ForeignKey(help_text='Укажите названине сборки.', on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.collection', verbose_name='Сборка')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collections', to='products.product', verbose_name='Продукт')),
            ],
        ),
    ]