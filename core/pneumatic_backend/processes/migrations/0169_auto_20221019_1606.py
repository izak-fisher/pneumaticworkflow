# Generated by Django 2.2.26 on 2022-10-19 16:06

from django.db import migrations, models
import django.db.models.deletion
import pneumatic_backend.generics.mixins.models


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0168_auto_20221018_2200'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checklist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('api_name', models.CharField(max_length=200)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='checklists', to='processes.Task')),
            ],
            options={
                'ordering': ('pk',),
            },
            bases=(pneumatic_backend.generics.mixins.models.SoftDeleteMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ChecklistTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('api_name', models.CharField(max_length=200)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='checklists', to='processes.TaskTemplate')),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='checklists', to='processes.Template')),
            ],
            options={
                'ordering': ('pk',),
            },
            bases=(pneumatic_backend.generics.mixins.models.SoftDeleteMixin, models.Model),
        ),
        migrations.AlterField(
            model_name='rawperformer',
            name='api_name',
            field=models.CharField(blank=True, help_text='For quick access to the api_name field ', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='rawperformertemplate',
            name='api_name',
            field=models.CharField(blank=True, help_text='For quick access to the api_name field ', max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='ChecklistTemplateSelection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('api_name', models.CharField(max_length=200)),
                ('value', models.CharField(max_length=200)),
                ('checklist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='selections', to='processes.ChecklistTemplate')),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='checklist_selections', to='processes.Template')),
            ],
            options={
                'ordering': ('pk',),
            },
            bases=(pneumatic_backend.generics.mixins.models.SoftDeleteMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ChecklistSelection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('api_name', models.CharField(max_length=200)),
                ('date_selected', models.DateTimeField(null=True)),
                ('selected_user_id', models.IntegerField(null=True)),
                ('value', models.CharField(max_length=200)),
                ('checklist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='selections', to='processes.Checklist')),
            ],
            options={
                'ordering': ('pk',),
            },
            bases=(pneumatic_backend.generics.mixins.models.SoftDeleteMixin, models.Model),
        ),
        migrations.AddConstraint(
            model_name='checklisttemplateselection',
            constraint=models.UniqueConstraint(condition=models.Q(is_deleted=False), fields=('template', 'api_name'), name='processes_checklisttemplateselection_template_api_name_unique'),
        ),
        migrations.AddConstraint(
            model_name='checklisttemplate',
            constraint=models.UniqueConstraint(condition=models.Q(is_deleted=False), fields=('template', 'api_name'), name='processes_checklisttemplate_template_api_name_unique'),
        ),
    ]
