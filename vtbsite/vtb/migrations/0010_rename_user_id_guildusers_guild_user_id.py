# Generated by Django 4.1.2 on 2022-10-08 03:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vtb', '0009_remove_users_guild'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guildusers',
            old_name='user_id',
            new_name='guild_user_id',
        ),
    ]
