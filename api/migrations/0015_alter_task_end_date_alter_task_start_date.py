# Generated by Django 4.0.2 on 2022-03-10 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_task_end_date_task_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='end_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='task',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]
