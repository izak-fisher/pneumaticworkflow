# Generated by Django 2.2.17 on 2021-01-22 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0102_auto_20201224_0921'),
    ]

    operations = [
        migrations.AddField(
            model_name='fieldtemplate',
            name='task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fields', to='processes.TaskWorkflow'),
        ),
    ]