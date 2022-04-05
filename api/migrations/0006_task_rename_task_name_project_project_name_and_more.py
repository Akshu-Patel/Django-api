# Generated by Django 4.0.2 on 2022-03-09 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=200)),
                ('developer', models.CharField(max_length=200)),
                ('status', models.BooleanField()),
            ],
        ),
        migrations.RenameField(
            model_name='project',
            old_name='task_name',
            new_name='project_name',
        ),
        migrations.RemoveField(
            model_name='enroll',
            name='admin',
        ),
        migrations.RemoveField(
            model_name='enroll',
            name='project_developer',
        ),
        migrations.RemoveField(
            model_name='enroll',
            name='project_manager',
        ),
    ]