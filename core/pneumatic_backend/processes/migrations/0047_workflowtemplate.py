# Generated by Django 2.2.14 on 2020-07-22 10:38

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
from pneumatic_backend.generics.mixins.models import SoftDeleteMixin


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0046_auto_20200715_1255'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkflowTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('name', models.CharField(blank=True, max_length=64, null=True)),
                ('workflow_template', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(SoftDeleteMixin, models.Model),
        ),
    ]