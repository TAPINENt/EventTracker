# Generated by Django 4.0.4 on 2022-08-03 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0006_merge_20220731_1544'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event_socials',
            name='is_event_guest',
        ),
        migrations.RemoveField(
            model_name='event_socials',
            name='is_event_host',
        ),
        migrations.RemoveField(
            model_name='event_socials',
            name='is_event_performer',
        ),
    ]