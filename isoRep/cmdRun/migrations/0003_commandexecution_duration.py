# Generated by Django 4.2.2 on 2023-06-21 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdRun', '0002_rename_executed_at_commandexecution_start_execution_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='commandexecution',
            name='duration',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
