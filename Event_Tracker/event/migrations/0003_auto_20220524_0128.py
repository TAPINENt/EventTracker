# Generated by Django 2.2.28 on 2022-05-24 01:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20220524_0127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_code',
            field=models.UUIDField(default=uuid.UUID('b1ea0cbe-8912-42ea-8f5a-79e8f217756f'), editable=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_code_short',
            field=models.CharField(default='ZfL9frp', max_length=10),
        ),
    ]
