# Generated by Django 3.2.15 on 2022-12-10 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20221119_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='position',
            field=models.CharField(blank=True, help_text='Укажите должность контакта.', max_length=200, null=True, verbose_name='Должность'),
        ),
    ]