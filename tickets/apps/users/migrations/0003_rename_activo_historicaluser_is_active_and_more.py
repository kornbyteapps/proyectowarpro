# Generated by Django 4.0.6 on 2022-08-01 05:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_historicaluser_is_active_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicaluser',
            old_name='activo',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='activo',
            new_name='is_active',
        ),
    ]