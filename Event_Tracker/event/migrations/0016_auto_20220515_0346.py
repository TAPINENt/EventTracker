# Generated by Django 2.2.27 on 2022-05-15 03:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0015_auto_20220515_0346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_code',
            field=models.UUIDField(default=uuid.UUID('b6ecd6a9-ccfe-42aa-a7f5-dc5c31d349ec'), editable=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_code_short',
            field=models.CharField(default='aZ9mMAa', max_length=10),
        ),
    ]
