# Generated by Django 2.2.16 on 2020-10-22 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0081_workflowtemplate_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='fieldtemplate',
            name='default',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='workflowtemplate',
            name='type',
            field=models.CharField(choices=[('generic', 'Generic workflows'), ('owner_onboarding', 'Account owners onboarding workflow')], default='generic', max_length=16),
        ),
    ]