# Generated by Django 5.0.8 on 2024-08-08 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0003_alter_department_parent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='department',
            options={'verbose_name': ('Отдел',), 'verbose_name_plural': 'Отделы'},
        ),
    ]
