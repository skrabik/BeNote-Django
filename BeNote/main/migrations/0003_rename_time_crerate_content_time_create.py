# Generated by Django 4.1.7 on 2023-05-26 23:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_content_last_time_update_content_time_crerate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='content',
            old_name='time_crerate',
            new_name='time_create',
        ),
    ]
