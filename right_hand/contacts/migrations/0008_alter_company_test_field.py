# Generated by Django 3.2.15 on 2023-02-03 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0007_auto_20230203_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='test_field',
            field=models.CharField(blank=True, default=1, max_length=10),
            preserve_default=False,
        ),
    ]