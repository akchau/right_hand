# Generated by Django 3.2.15 on 2022-10-16 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0021_alter_company_fact_adress'),
        ('tasks', '0006_alter_task_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='interest',
            name='main_contact',
            field=models.ForeignKey(help_text='Укажите контакт который работает в этой компании.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='interests', to='contacts.contact', verbose_name='Основной контакт'),
        ),
    ]
