# Generated by Django 2.2.28 on 2022-05-04 02:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_auto_20220504_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_code',
            field=models.UUIDField(default=uuid.UUID('87325778-2d74-4c30-9065-d20c2bc8b686'), editable=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_code_short',
            field=models.CharField(default='S57ZGKa', max_length=10),
        ),
    ]