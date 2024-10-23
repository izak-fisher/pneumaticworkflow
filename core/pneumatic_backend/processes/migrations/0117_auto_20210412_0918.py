# Generated by Django 2.2.17 on 2021-04-12 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0116_populate_task_api_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskworkflow',
            name='api_name',
            field=models.CharField(max_length=160),
        ),
        migrations.AddConstraint(
            model_name='taskworkflow',
            constraint=models.UniqueConstraint(condition=models.Q(is_deleted=False), fields=('workflow', 'api_name'), name='processes_taskworkflow_workflow_api_name_unique'),
        ),
    ]