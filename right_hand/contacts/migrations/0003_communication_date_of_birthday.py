# Generated by Django 3.2.15 on 2022-09-26 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_contact_frequency_of_communications_days'),
    ]

    operations = [
        migrations.AddField(
            model_name='communication',
            name='date_of_birthday',
            field=models.DateTimeField(blank=True, default='2011-09-29', verbose_name='Дата рождения.'),
        ),
    ]
