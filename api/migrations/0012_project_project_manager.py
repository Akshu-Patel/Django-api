# Generated by Django 4.0.2 on 2022-03-10 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_enroll_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_manager',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='api.enroll', to_field='username'),
        ),
    ]
