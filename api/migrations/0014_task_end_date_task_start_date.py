# Generated by Django 4.0.2 on 2022-03-10 09:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_task_project_alter_project_name_alter_task_developer'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='task',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
