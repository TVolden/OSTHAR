# Generated by Django 5.0.2 on 2024-02-12 10:43

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studies', '0003_alter_study_localtime_alter_study_servertime'),
    ]

    operations = [
        migrations.AddField(
            model_name='study',
            name='localendtime',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='study',
            name='serverendtime',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='study',
            name='session',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
