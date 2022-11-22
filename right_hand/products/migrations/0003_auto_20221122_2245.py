# Generated by Django 3.2.15 on 2022-11-22 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20221119_1505'),
        ('products', '0002_alter_product_unit'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='collection',
            options={'verbose_name': 'Сборка', 'verbose_name_plural': 'Сборки'},
        ),
        migrations.AddField(
            model_name='product',
            name='maker',
            field=models.ForeignKey(help_text='Укажите произоводителя', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='contacts.company', verbose_name='Производитель'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='name',
            field=models.CharField(help_text='Укажите название сборки.', max_length=200, verbose_name='Название сборки'),
        ),
        migrations.AlterField(
            model_name='product',
            name='unit',
            field=models.CharField(choices=[('кг', 'кг'), ('м', 'м'), ('шт', 'шт')], max_length=10, verbose_name='Еденица измерения'),
        ),
    ]
