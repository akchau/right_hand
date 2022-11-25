# Generated by Django 3.2.15 on 2022-11-25 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_task_next_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название категории.', max_length=200, verbose_name='Название категории.')),
            ],
        ),
        migrations.RemoveField(
            model_name='task',
            name='next_task',
        ),
        migrations.AddField(
            model_name='task',
            name='category',
            field=models.ForeignKey(help_text='Укажите категорию задачи.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tasks', to='tasks.categorytask', verbose_name='Категория задачи.'),
        ),
    ]
