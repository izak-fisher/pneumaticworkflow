# Generated by Django 2.2 on 2023-04-27 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0101_auto_20230410_0742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='is_onboarding_finished',
        ),
        migrations.AddField(
            model_name='account',
            name='payment_card_provided',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='notification',
            name='type',
            field=models.CharField(choices=[('system', 'system'), ('comment', 'new comment'), ('mention', 'mention'), ('urgent', 'urgent'), ('not_urgent', 'not urgent'), ('overdue_task', 'overdue task'), ('snooze_workflow', 'snooze workflow'), ('resume_workflow', 'resume workflow'), ('due_date_changed', 'due date changed')], max_length=24),
        ),
    ]
