# Generated by Django 2.2.27 on 2022-05-13 15:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0013_auto_20220513_0345'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='auth_user',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_code',
            field=models.UUIDField(default=uuid.UUID('1ef7a6ae-bd2e-4850-9e29-da68aa69bcde'), editable=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_code_short',
            field=models.CharField(default='7X5CZf2', max_length=10),
        ),
    ]
