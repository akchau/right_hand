# Generated by Django 3.2.15 on 2022-10-01 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0009_alter_communication_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inn', models.CharField(max_length=10, verbose_name='ИНН')),
                ('kpp', models.CharField(max_length=9, verbose_name='КПП')),
                ('ogrn', models.CharField(max_length=13, verbose_name='ОГРН')),
                ('okpo', models.CharField(max_length=10, verbose_name='ОКПО')),
                ('okved', models.CharField(max_length=10, verbose_name='ОКВЭД')),
                ('fact_adress', models.TextField()),
                ('legal_adress', models.TextField()),
                ('full_name', models.CharField(max_length=150, verbose_name='Полное наименование')),
                ('short_name', models.CharField(max_length=150, verbose_name='Полное наименование')),
                ('main_email', models.EmailField(max_length=254, verbose_name='Основной email')),
                ('phone_number', models.CharField(max_length=30, verbose_name='Номер телефона')),
                ('number_acount', models.CharField(max_length=20, verbose_name='Расчетный счет')),
                ('cor_acount', models.CharField(max_length=20, verbose_name='Корреспондентский счет')),
                ('bic', models.CharField(max_length=9, verbose_name='БИК')),
                ('head_of_company', models.CharField(max_length=200, verbose_name='ФИО руководителя')),
            ],
        ),
        migrations.AlterField(
            model_name='communication',
            name='info',
            field=models.TextField(blank=True, default='Нет описания', help_text='Добавьте описние', null=True, verbose_name='Описание коммуникации'),
        ),
        migrations.AlterField(
            model_name='communication',
            name='type',
            field=models.CharField(choices=[('Звонок', 'Звонок'), ('Встреча', 'Встреча'), ('Переписка', 'Переписка'), ('Видео-звонок', 'Видео-звонок')], max_length=20),
        ),
    ]
