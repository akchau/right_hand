# Generated by Django 3.2.15 on 2022-11-27 22:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20221119_1505'),
        ('tasks', '0011_auto_20221128_0020'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='plan_pomodoro',
            field=models.SmallIntegerField(default=1, help_text='Укажите, кол-во 30-минутных отрезков на задачу.', verbose_name='Временная сложность задачи'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='customer',
            field=models.ForeignKey(blank=True, help_text='Укажите заказчика.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projects', to='contacts.company', verbose_name='Заказчик'),
        ),
    ]
