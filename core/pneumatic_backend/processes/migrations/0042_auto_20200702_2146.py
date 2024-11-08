# Generated by Django 2.2.13 on 2020-07-02 21:46

from django.db import migrations, models
import django.db.models.deletion
from pneumatic_backend.generics.mixins.models import SoftDeleteMixin


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0042_auto_20200624_1054'),
        ('processes', '0041_merge_20200701_1408'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fieldtemplate',
            name='task',
        ),
        migrations.AddField(
            model_name='taskfield',
            name='api_name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='taskfield',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='output', to='processes.Task'),
        ),
        migrations.CreateModel(
            name='TaskWorkflowOutput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Account')),
                ('task', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='output', to='processes.TaskWorkflow')),
            ],
            options={
                'abstract': False,
            },
            bases=(SoftDeleteMixin, models.Model),
        ),
        migrations.CreateModel(
            name='FieldSelection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('value', models.CharField(max_length=200)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='selections', to='processes.TaskField')),
            ],
            options={
                'abstract': False,
            },
            bases=(SoftDeleteMixin, models.Model),
        ),
        migrations.AddField(
            model_name='fieldtemplate',
            name='task_output',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fields', to='processes.TaskWorkflowOutput'),
        ),
    ]
