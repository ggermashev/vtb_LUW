# Generated by Django 4.1.2 on 2022-10-08 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vtb', '0006_alter_categories_options_alter_roles_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guilds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guildName', models.CharField(max_length=16)),
                ('guildPoints', models.IntegerField()),
                ('guildRanking', models.CharField(max_length=4)),
            ],
        ),
        migrations.AlterModelOptions(
            name='taskfilters',
            options={'verbose_name': 'Фильтры заданий', 'verbose_name_plural': 'Фильтры заданий'},
        ),
        migrations.AddField(
            model_name='users',
            name='guild',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='vtb.guilds'),
        ),
    ]
