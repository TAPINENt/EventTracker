# Generated by Django 2.2.27 on 2022-04-27 00:46

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20220421_1536'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='event_host',
            new_name='host',
        ),
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
        migrations.AddField(
            model_name='event_host',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='event.Event'),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_code',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='event_socials',
            name='social_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='event_users',
            name='user_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
