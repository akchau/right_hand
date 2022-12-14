# Generated by Django 3.2.15 on 2022-10-26 15:11

import contacts.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inn', models.CharField(help_text='Укажите ИНН.', max_length=12, validators=[contacts.validators.validate_inn], verbose_name='ИНН')),
                ('kpp', models.CharField(blank=True, help_text='Укажите КПП.', max_length=9, null=True, verbose_name='КПП')),
                ('ogrn', models.CharField(blank=True, help_text='Укажите ОГРН.', max_length=13, null=True, verbose_name='ОГРН')),
                ('okpo', models.CharField(blank=True, help_text='Укажите ОКПО.', max_length=10, null=True, verbose_name='ОКПО')),
                ('okved', models.CharField(blank=True, help_text='Укажите ОКВЭД.', max_length=10, null=True, verbose_name='ОКВЭД')),
                ('fact_adress', models.TextField(blank=True, help_text='Укажите фактический адрес.', null=True, verbose_name='Фактический адрес')),
                ('legal_adress', models.TextField(help_text='Укажите юридический адрес.', verbose_name='Юридический адрес')),
                ('full_name', models.CharField(help_text='Укажите полное наименование.', max_length=200, verbose_name='Полное наименование')),
                ('short_name', models.CharField(help_text='Укажите сокращенное наименование.', max_length=150, verbose_name='Сокращенное наименование')),
                ('main_email', models.EmailField(blank=True, help_text='Укажите основной email.', max_length=254, null=True, verbose_name='Основной email')),
                ('number_acount', models.CharField(blank=True, help_text='Укажите номер расчетного счета.', max_length=20, null=True, verbose_name='Расчетный счет')),
                ('cor_acount', models.CharField(blank=True, help_text='Укажите номер кореспондентского счета.', max_length=20, null=True, verbose_name='Корреспондентский счет')),
                ('bic', models.CharField(blank=True, help_text='Укажите БИК банка.', max_length=9, null=True, verbose_name='БИК')),
                ('head_of_company', models.CharField(blank=True, help_text='Укажите ФИО руководителя компании.', max_length=200, null=True, verbose_name='ФИО руководителя')),
                ('mobile_number_of_head', models.CharField(blank=True, help_text='Укажите номер телефона.', max_length=30, null=True, validators=[contacts.validators.validate_mobile_phone_number], verbose_name='Мобильный телефон директора.')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Укажите фамилию и имя контакта.', max_length=200, verbose_name='Имя контакта')),
                ('role', models.CharField(blank=True, choices=[('Член семьи', 'Член семьи'), ('Подчиненый', 'Подчиненый'), ('Товарищ', 'Товарищ'), ('Коллега', 'Коллега'), ('Деловой партнер', 'Деловой партнер')], help_text='Выберите роль контакта.', max_length=20, null=True, verbose_name='Роль контакта')),
                ('email', models.EmailField(blank=True, help_text='Укажите основной email.', max_length=254, null=True, verbose_name='Email')),
                ('mobile_phone_number', models.CharField(blank=True, help_text='Укажите номер телефона.', max_length=30, null=True, validators=[contacts.validators.validate_mobile_phone_number], verbose_name='Мобильный телефон')),
                ('frequency_of_communications_days', models.IntegerField(help_text='Укажите как часто хотите общаться с контактом.', verbose_name='Частота коммуникаций. Раз/дней.')),
                ('date_of_birthday', models.DateTimeField(blank=True, help_text='Укажите день рождения контакта.', null=True, verbose_name='Дата рождения.')),
                ('position', models.CharField(help_text='Укажите должность контакта.', max_length=200, verbose_name='Должность')),
                ('company', models.ForeignKey(blank=True, help_text='Укажите компанию контакта.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='company', to='contacts.company', verbose_name='Компания')),
            ],
        ),
        migrations.CreateModel(
            name='Communication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Звонок', 'Звонок'), ('Встреча', 'Встреча'), ('Переписка', 'Переписка'), ('Видео-звонок', 'Видео-звонок')], help_text='Укажите тип комуникации.', max_length=20, verbose_name='Тип коммуникации.')),
                ('status', models.CharField(blank=True, choices=[('Выполнено', 'Выполнено'), ('Запланировано', 'Запланировано')], help_text='Укажите статус коммуникации.', max_length=20, null=True, verbose_name='Статус.')),
                ('pub_date', models.DateTimeField(auto_now_add=True, help_text='Дата создания коммуникации.', verbose_name='Дата создания объекта коммуникации.')),
                ('plan_date', models.DateTimeField(blank=True, help_text='Планируемая дата коммуникации.', null=True, verbose_name='Планируемая дата коммуникации.')),
                ('done_date', models.DateTimeField(blank=True, help_text='Планируемая дата взаимодействия.', null=True, verbose_name='Дата коммуникации.')),
                ('info', models.TextField(blank=True, default='Нет описания', help_text='Добавьте описние', null=True, verbose_name='Описание коммуникации')),
                ('contact', models.ForeignKey(help_text='Укажите контакт коммуникаиции.', on_delete=django.db.models.deletion.CASCADE, related_name='communication', to='contacts.contact', verbose_name='Контакт')),
            ],
        ),
    ]
