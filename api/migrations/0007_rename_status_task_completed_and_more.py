# Generated by Django 4.0.2 on 2022-03-09 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_task_rename_task_name_project_project_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='status',
            new_name='completed',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_name',
        ),
    ]