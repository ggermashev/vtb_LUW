# Generated by Django 4.1.2 on 2022-10-08 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vtb', '0015_remove_tasks_min_exp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasks',
            name='filter',
        ),
        migrations.RemoveField(
            model_name='tasks',
            name='time_created',
        ),
    ]
