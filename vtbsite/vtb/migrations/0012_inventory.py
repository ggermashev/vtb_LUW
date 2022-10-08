# Generated by Django 4.1.2 on 2022-10-08 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vtb', '0011_users_privatekey_users_publickey'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('good_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vtb.goods')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vtb.users')),
            ],
        ),
    ]