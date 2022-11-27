# Generated by Django 3.2.15 on 2022-11-27 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0009_task_interest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.ForeignKey(blank=True, help_text='Укажите категорию задачи.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tasks', to='tasks.categorytask', verbose_name='Категория задачи.'),
        ),
    ]