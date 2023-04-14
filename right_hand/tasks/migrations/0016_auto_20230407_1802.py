# Generated by Django 3.2.15 on 2023-04-07 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0015_alter_task_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Criterion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Уажите критерий.', max_length=200, verbose_name='Критерий')),
            ],
        ),
        migrations.RemoveField(
            model_name='task',
            name='category',
        ),
        migrations.AddField(
            model_name='task',
            name='category',
            field=models.ManyToManyField(to='tasks.CategoryTask'),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Создан', 'Создан'), ('Не выполнен', 'Не выполнен'), ('В работе', 'В работе'), ('Завершен', 'Завершен')], max_length=20, verbose_name='Статус задачи'),
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Уажите цель.', max_length=200, verbose_name='Цель')),
                ('deadline', models.DateTimeField(help_text='Дедлайн цели.', verbose_name='Дедлайн цели')),
                ('criterion', models.ManyToManyField(to='tasks.Criterion')),
            ],
        ),
    ]