# Generated by Django 4.1.2 on 2022-10-07 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vtb', '0002_users_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskFilters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filter', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=256)),
                ('reward', models.IntegerField()),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('min_exp', models.IntegerField()),
                ('filter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='vtb.taskfilters')),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=256)),
                ('reward', models.IntegerField()),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='vtb.users')),
            ],
        ),
    ]
