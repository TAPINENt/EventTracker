# Generated by Django 2.2.27 on 2022-04-22 02:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20220421_1536'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event_host',
            old_name='host_id',
            new_name='host',
        ),
        migrations.RenameField(
            model_name='event_host',
            old_name='social_id',
            new_name='social',
        ),
    ]
