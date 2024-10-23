# Generated by Django 2.2.16 on 2020-11-02 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0085_auto_20201029_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workflowtemplate',
            name='type',
            field=models.CharField(choices=[('generic', 'Generic workflows'), ('owner_onboarding', 'Account owners onboarding workflow'), ('invited_onboarding', 'Invited admin users onboarding workflow'), ('invited_onboarding_admin', 'Invited admin users onboarding workflow'), ('invited_onboarding_regular', 'Invited regular users onboarding workflow')], default='generic', max_length=48),
        ),
    ]
