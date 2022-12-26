# Generated by Django 3.2.15 on 2022-12-26 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0013_task_done_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(blank=True, choices=[('Не выполнен', 'Не выполнен'), ('В работе', 'В работе'), ('Завершен', 'Завершен')], max_length=20, null=True, verbose_name='Статус задачи'),
        ),
    ]
