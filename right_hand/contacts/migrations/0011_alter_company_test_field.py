# Generated by Django 3.2.15 on 2023-02-06 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0010_alter_company_test_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='test_field',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
