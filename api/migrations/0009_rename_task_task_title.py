# Generated by Django 4.0.2 on 2022-03-09 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_rename_task_name_task_task'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='task',
            new_name='title',
        ),
    ]