# Generated by Django 2.2.16 on 2020-10-26 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0083_auto_20201022_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workflowtemplate',
            name='name',
            field=models.CharField(max_length=64),
        ),
    ]
