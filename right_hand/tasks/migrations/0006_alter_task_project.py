# Generated by Django 3.2.15 on 2022-10-16 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_auto_20221015_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='project',
            field=models.ForeignKey(blank=True, help_text='Укажите к какому проекту относится задача.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='tasks.project', verbose_name='Проект'),
        ),
    ]
