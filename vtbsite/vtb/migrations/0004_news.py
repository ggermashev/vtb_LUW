# Generated by Django 4.1.2 on 2022-10-07 23:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vtb', '0003_taskfilters_tasks_events'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_news', models.CharField(max_length=64)),
                ('content', models.CharField(max_length=512)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='User', to='vtb.users')),
            ],
        ),
    ]
