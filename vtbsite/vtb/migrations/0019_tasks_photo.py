# Generated by Django 4.1.2 on 2022-10-08 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vtb', '0018_tasks_description_tasks_name_tasks_reward'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='photo',
            field=models.ImageField(null=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
